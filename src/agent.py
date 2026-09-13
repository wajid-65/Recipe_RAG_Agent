"""
Agent assembly.

Built on langgraph.prebuilt.create_react_agent -- the current, actively
maintained agent construction pattern. LangChain's older
AgentExecutor/create_tool_calling_agent (used in earlier versions of
this project) was removed in langchain 1.0 and is no longer available.

This also gets automatic "thought signature" handling for Gemini's
newer thinking models (required for multi-turn tool calling on Gemini 3.x)
for free, since it comes from the current langchain-google-genai package
built on Google's unified SDK -- the older package used the legacy SDK
and could not do this.

Conversation memory is handled by LangGraph's checkpointer (keyed by
thread_id) instead of RunnableWithMessageHistory.
"""
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.config import LLM_MODEL, LLM_TEMPERATURE, GROQ_API_KEY
from src.tools import (
    retrieve_recipes,
    what_can_i_cook,
    substitution_tool,
    nutrition_tool,
    shopping_list_tool,
    adapt_recipe_tool,
    _text,
)

STRUCTURED_OUTPUT_INSTRUCTIONS = """
When you give a final recipe answer, format it using this structure:

**Recipe Name:**
**Adaptations Made:** (diet / ingredients / time changes, or "None")
**Ingredients:** (mark any substitutions)
**Step-by-Step Instructions:**
1. ...
**Nutritional Facts (per serving):** (call NutritionEstimator if not already available)
**Shopping List:** (call ShoppingListGenerator if not already available)
**Sources:** (cite which retrieved document(s) this is based on)

If nothing relevant was found in the knowledge base, say so plainly
instead of inventing a recipe.
"""

SYSTEM_PROMPT = (
    "You are a helpful, precise recipe assistant. You have access to tools "
    "for retrieving recipes, matching ingredients, suggesting substitutions, "
    "adapting recipes, estimating nutrition, and building shopping lists. "
    "Always ground recipe facts in RecipeRetriever/WhatCanICook results -- "
    "never invent a recipe that isn't in the knowledge base. "
    f"{STRUCTURED_OUTPUT_INSTRUCTIONS}"
)

# Shared checkpointer so conversation state persists across calls to ask()
# within the same process, keyed by thread_id (== our session_id).
_checkpointer = InMemorySaver()


def build_agent(vectorstore):
    """
    Builds the full tool-using, memory-aware agent powered by Groq.
    """
    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=LLM_TEMPERATURE,
        max_tokens=1024,
        groq_api_key=GROQ_API_KEY,
    )


    # Tools are defined as closures over `vectorstore` so the retrieval
    # tools can search it without the agent needing to pass it around.
    @tool
    def RecipeRetriever(query: str) -> str:
        """Search the recipe knowledge base for information relevant to a
        cooking question. Use this first for any question about a specific
        recipe, dish, or cooking technique."""
        return retrieve_recipes(vectorstore, query)

    @tool
    def WhatCanICook(ingredients: str) -> str:
        """Given a comma-separated list of ingredients the user currently
        has, find the best-matching recipe(s) from the knowledge base and
        list what's missing. Input should be a plain comma-separated
        ingredient list, e.g. 'eggs, flour, milk, bananas'."""
        return what_can_i_cook(vectorstore, ingredients)

    @tool
    def SubstitutionAdvisor(query: str) -> str:
        """Suggest ingredient substitutions for dietary restrictions or an
        unavailable ingredient. Input: a short description, e.g.
        'substitute for sugar in chocolate cake, diabetic-friendly'."""
        return substitution_tool(query)

    @tool
    def AdaptRecipe(recipe_text: str, constraints: str) -> str:
        """Adapt a full recipe to meet constraints (diet, time, cuisine).
        recipe_text is the full original recipe (ingredients + steps).
        constraints describes what to change, e.g. 'make it vegan and
        under 30 minutes'."""
        return adapt_recipe_tool(recipe_text, constraints)

    @tool
    def NutritionEstimator(recipe_text: str) -> str:
        """Estimate nutrition facts (calories, protein, carbs, fat) per
        serving for a given recipe. Input: the full recipe text
        (ingredients + steps)."""
        return nutrition_tool(recipe_text)

    @tool
    def ShoppingListGenerator(recipe_text: str) -> str:
        """Generate a structured shopping list (item + quantity) from a
        recipe. Input: the full recipe text (ingredients + steps)."""
        return shopping_list_tool(recipe_text)

    tools = [
        RecipeRetriever,
        WhatCanICook,
        SubstitutionAdvisor,
        AdaptRecipe,
        NutritionEstimator,
        ShoppingListGenerator,
    ]

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=SYSTEM_PROMPT,
        checkpointer=_checkpointer,
    )

    return agent


def ask(agent, user_input: str, session_id: str = "default") -> str:
    """
    Convenience wrapper for a single conversational turn. session_id maps
    to LangGraph's thread_id, which is how conversation history/state is
    kept separate between different sessions.

    If the stored history for this session is corrupted (e.g. an interrupted
    tool call left a dangling AIMessage with no ToolMessage), we detect that
    ValueError, discard the bad thread, and retry transparently so the user
    never sees the crash.
    """
    import uuid as _uuid

    def _invoke(sid: str):
        return agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"configurable": {"thread_id": sid}},
        )

    try:
        result = _invoke(session_id)
    except ValueError as exc:
        if "tool_calls that do not have" in str(exc) or "INVALID_CHAT_HISTORY" in str(exc):
            # History is corrupted — retry with a fresh thread to discard bad state
            fresh_id = f"{session_id}-retry-{_uuid.uuid4().hex[:6]}"
            print("[agent] Detected corrupted session history. Starting fresh for this query.")
            result = _invoke(fresh_id)
        else:
            raise
    # The last message in the returned state is the agent's final answer.
    return _text(result["messages"][-1].content)
