"""
Agent tools for the Recipe RAG Agent.

Each tool is a plain Python function wrapped as a LangChain Tool in
agent.py. Kept here as standalone functions so they can also be
unit-tested or called directly without going through the agent.
"""
import json
import re
from typing import List, Optional

from langchain_core.documents import Document
from langchain_groq import ChatGroq

from src.config import LLM_MODEL, LLM_TEMPERATURE, GROQ_API_KEY
from src.vectorstore import filtered_retrieve

_llm = None


def _get_llm() -> ChatGroq:
    global _llm
    if _llm is None:
        _llm = ChatGroq(
            model=LLM_MODEL,
            temperature=LLM_TEMPERATURE,
            max_tokens=1024,
            groq_api_key=GROQ_API_KEY,
        )
    return _llm




import unicodedata


def _text(content) -> str:
    """
    Normalizes an LLM message's .content to a plain string.
    Removes non-standard unicode hyphens/spaces (like \u2011, \u202f) that cause Windows cp1252 stdout errors.
    """
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                if block.get("type") in (None, "text") and "text" in block:
                    parts.append(block["text"])
        res_str = "".join(parts).strip()
    else:
        res_str = str(content)
    
    # Normalize special unicode characters for clean display across all platforms
    res_str = unicodedata.normalize('NFKC', res_str)
    res_str = res_str.replace('\u2011', '-').replace('\u202f', ' ').replace('\xa0', ' ')
    return res_str




# ---------------------------------------------------------------------
# 1. Grounded recipe retrieval (with source citation + fallback)
# ---------------------------------------------------------------------
def retrieve_recipes(vectorstore, query: str, cuisine: Optional[str] = None,
                      diet_tag: Optional[str] = None, max_time_minutes: Optional[int] = None) -> str:
    """
    Retrieves relevant recipe chunks and answers ONLY from that context.
    Explicitly returns a "not found" signal if nothing relevant is
    retrieved, instead of letting the LLM hallucinate a recipe.
    """
    docs: List[Document] = filtered_retrieve(
        vectorstore, query, cuisine=cuisine, diet_tag=diet_tag, max_time_minutes=max_time_minutes
    )

    if not docs:
        return "NO_MATCH: No relevant recipe found in the knowledge base for this query."

    context_blocks = []
    for i, d in enumerate(docs, 1):
        context_blocks.append(
            f"[Source {i}: {d.metadata.get('title', 'Untitled')} "
            f"({d.metadata.get('source', 'unknown')})]\n{d.page_content}"
        )
    context = "\n\n".join(context_blocks)

    prompt = f"""You are a recipe assistant. Answer the user's question using ONLY
the recipe context below. If the context does not contain enough
information to answer, say so explicitly instead of guessing.
Cite which source number(s) you used.

Context:
{context}

Question: {query}

Answer (cite sources like [Source 1]):"""

    response = _get_llm().invoke(prompt)
    return _text(response.content)


# ---------------------------------------------------------------------
# 2. Ingredient-based "what can I cook" tool
# ---------------------------------------------------------------------
def what_can_i_cook(vectorstore, available_ingredients: str, k: int = 6) -> str:
    """
    Given a comma-separated list of ingredients the user has on hand,
    finds recipes that best match, ranked by overlap, and tells the
    user what's missing for each.
    """
    ingredients = [i.strip().lower() for i in available_ingredients.split(",") if i.strip()]
    if not ingredients:
        return "Please list at least one ingredient you have available."

    query = "recipe using " + ", ".join(ingredients)
    docs = filtered_retrieve(vectorstore, query, k=max(k, 10))

    if not docs:
        return "NO_MATCH: No recipes found matching those ingredients."

    context_blocks = []
    for i, d in enumerate(docs, 1):
        context_blocks.append(f"[Source {i}: {d.metadata.get('title','Untitled')}]\n{d.page_content}")
    context = "\n\n".join(context_blocks)

    prompt = f"""The user has these ingredients available: {', '.join(ingredients)}.

Using ONLY the recipes in the context below, identify the recipe(s) that
best match what the user already has. For each candidate recipe:
- Name it and cite the source
- List which of the user's ingredients it uses
- List what additional ingredients (if any) they'd still need to buy

If none of the recipes are a reasonable match, say so clearly.

Context:
{context}
"""
    response = _get_llm().invoke(prompt)
    return _text(response.content)


# ---------------------------------------------------------------------
# 3. Substitution tool
# ---------------------------------------------------------------------
def substitution_tool(query: str) -> str:
    """
    Suggests ingredient substitutions for dietary restrictions or
    unavailable ingredients. Not grounded in retrieval (general
    culinary knowledge), used as a secondary/support tool.
    """
    prompt = f"""Suggest practical ingredient substitutions for: {query}

For each substitution, briefly note:
- The ratio/quantity adjustment (if any)
- Any effect on taste, texture, or cooking time
Keep it concise and actionable."""
    return _text(_get_llm().invoke(prompt).content)


# ---------------------------------------------------------------------
# 4. Nutrition estimator tool
# ---------------------------------------------------------------------
def nutrition_tool(recipe_text: str) -> str:
    """
    Estimates per-serving nutrition facts for a given recipe text.
    Returns structured JSON so it can be rendered visually downstream.
    """
    prompt = f"""Estimate approximate nutrition facts per serving for this recipe.
Return ONLY valid JSON with this exact shape, no other text:

{{
  "servings": <int>,
  "calories": <int>,
  "protein_g": <int>,
  "carbs_g": <int>,
  "fat_g": <int>,
  "note": "<brief caveat that this is an estimate>"
}}

Recipe:
{recipe_text}"""
    response = _text(_get_llm().invoke(prompt).content)
    cleaned = re.sub(r"```json|```", "", response).strip()
    try:
        return json.dumps(json.loads(cleaned), indent=2)
    except Exception:
        return json.dumps({
            "servings": None, "calories": None, "protein_g": None,
            "carbs_g": None, "fat_g": None,
            "note": "Could not parse nutrition estimate from model output."
        }, indent=2)


# ---------------------------------------------------------------------
# 5. Shopping list generator
# ---------------------------------------------------------------------
def shopping_list_tool(recipe_text: str) -> str:
    """
    Extracts a clean shopping list (ingredient + quantity) as JSON,
    ready to render as a checklist.
    """
    prompt = f"""Extract a shopping list from this recipe.
Return ONLY valid JSON: a list of objects like
{{"item": "<ingredient>", "quantity": "<amount>"}}
Combine duplicate ingredients. No other text.

Recipe:
{recipe_text}"""
    response = _text(_get_llm().invoke(prompt).content)
    cleaned = re.sub(r"```json|```", "", response).strip()
    try:
        parsed = json.loads(cleaned)
        return json.dumps(parsed, indent=2)
    except Exception:
        return json.dumps([{"item": "Could not parse shopping list", "quantity": ""}], indent=2)


# ---------------------------------------------------------------------
# 6. Recipe adaptation tool (diet / time / cuisine constraints)
# ---------------------------------------------------------------------
def adapt_recipe_tool(recipe_text: str, constraints: str) -> str:
    """
    Rewrites a retrieved recipe to satisfy user constraints
    (e.g. "make it vegan and under 30 minutes").
    """
    prompt = f"""Adapt the following recipe to satisfy these constraints: {constraints}

Keep the adaptation grounded in the original recipe -- do not invent an
unrelated dish. Clearly mark every change you made.

Original recipe:
{recipe_text}

Respond with:
**Adaptations Made:**
**Adapted Ingredients:**
**Adapted Steps:**"""
    return _text(_get_llm().invoke(prompt).content)
