# Recipe RAG Agent

A Document Q&A RAG agent that ingests recipe documents (PDFs, text/markdown
notes, web pages) into a FAISS vector store, and answers cooking questions
with personalization (diet, ingredients, time, cuisine), substitutions,
nutrition estimates, shopping lists, and an HTML visual output.

## Project Structure

```
recipe_rag_agent/
├── data/
│   ├── pdfs/              # drop cookbook / recipe PDFs here
│   ├── text_notes/        # .txt / .md recipe notes (2 samples included)
│   └── urls.txt           # one recipe blog URL per line
├── faiss_index/           # generated FAISS index (created on first build)
├── outputs/                # generated HTML visualizations
├── src/
│   ├── config.py           # paths, model names, chunk sizes, tag vocab
│   ├── metadata.py          # rule-based cuisine/diet/time tagging
│   ├── ingest.py            # PDF / text / web loaders
│   ├── chunking.py          # recipe-aware chunking + tagging
│   ├── vectorstore.py       # FAISS build/load/merge + filtered search
│   ├── tools.py             # retriever, ingredient-matcher, substitution,
│   │                         # nutrition, shopping-list, adapt-recipe tools
│   ├── agent.py             # history-aware retriever + tool-calling agent
│   └── visualize.py         # renders agent output as a styled HTML page
├── main.py                  # CLI entrypoint
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# edit .env and add your GOOGLE_API_KEY (from Google AI Studio: https://aistudio.google.com/apikey)
```

## Usage

**1. Build the index** (reads everything under `data/`):
```bash
python main.py --build-index
```
Two sample recipes are already included (`chocolate_cake.md`,
`vegan_thai_curry.md`) so you can test immediately without adding your own
files.

**2. Interactive chat** (multi-turn, remembers context):
```bash
python main.py --chat
```
Example session:
```
You: How do I make a sugar-free version of chocolate cake?
Agent: ...
You: Now make it gluten-free too
Agent: ...   <- correctly resolves "it" using chat history
```

**3. Single question with HTML visualization:**
```bash
python main.py --ask "What can I cook with tofu, broccoli, and coconut milk?" --html
```
Opens `outputs/recipe_output.html` in your browser for a styled step
tracker, shopping checklist, and nutrition card.

## What each requirement maps to

| Requirement | Implementation |
|---|---|
| Ingest & index recipe documents | `ingest.py` (PDF/text/web loaders) + `chunking.py` (recipe-aware splitting) + `vectorstore.py` (FAISS) |
| Conversational Q&A | `agent.py` — `create_history_aware_retriever` rewrites follow-ups using chat history before retrieval |
| Personalization (diet/ingredients/time/cuisine) | `metadata.py` tags chunks; `filtered_retrieve()` filters by them; `WhatCanICook` tool matches on available ingredients; `AdaptRecipe` tool rewrites for constraints |
| Substitutions | `SubstitutionAdvisor` tool |
| Nutrition facts | `NutritionEstimator` tool (structured JSON output) |
| Shopping list | `ShoppingListGenerator` tool (structured JSON output) |
| Visual step-by-step guidance | `visualize.py` renders an HTML page with numbered steps, checklist, nutrition card |
| Grounding / hallucination guardrail | `retrieve_recipes()` and `what_can_i_cook()` answer ONLY from retrieved context and return an explicit `NO_MATCH` signal when nothing relevant is found |

## Known limitations (be upfront about these if asked)

- Uses Google Gemini (`gemini-3.6-flash` for chat, `models/gemini-embedding-001` for embeddings) via `langchain-google-genai` 4.x, built on Google's current unified SDK. Google's model lineup moves fast — if `LLM_MODEL` in `config.py` ever throws a 404 "no longer available" error, the error message itself will tell you the exact replacement model string; just swap it in. Check https://ai.google.dev/gemini-api/docs/models for the current lineup any time.
- The agent is built with `langgraph.prebuilt.create_react_agent` (not the older `AgentExecutor`/`create_tool_calling_agent`, which LangChain removed in its 1.0 release). This also gets Gemini 3.x's required "thought signature" handling for multi-turn tool calls automatically — an older `langchain-google-genai` (built on Google's legacy SDK) can't do this and will error with `Function call is missing a thought_signature`.
- FAISS doesn't support native metadata filtering, so `filtered_retrieve()`
  over-fetches and filters in Python — fine at this scale, would need a
  different vector DB (Qdrant/Chroma) for very large corpora.
- Metadata tagging (`metadata.py`) is rule-based/regex, not LLM-based — fast
  and free, but will miss cuisines/diets not in `KNOWN_CUISINES` /
  `KNOWN_DIET_TAGS` in `config.py`. Extend those lists, or switch to the
  `llm_tag_chunk()` stub for higher accuracy at ingestion cost.
- Nutrition estimates are LLM-generated approximations, not verified against
  a nutrition database — clearly labeled as such in the output.
- No OCR — scanned/image-only PDFs will not extract text.
