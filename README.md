# Recipe RAG Agent (Groq + LangChain + LangGraph + Web UI)

An intelligent **Retrieval-Augmented Generation (RAG) Recipe Assistant** built with **LangChain**, **LangGraph**, **Groq LLM (`openai/gpt-oss-20b`)**, local **HuggingFace Embeddings (`all-MiniLM-L6-v2`)**, **FAISS Vector Store**, **FastAPI**, and a **Node.js/Express Web Interface**.

---

##  Key Features

- **100% Grounded RAG Architecture:** Answers recipe questions strictly using retrieved knowledge from verified recipe documents to eliminate AI hallucinations.
-  **Groq LLM Acceleration:** Powered by Groq's high-speed inference engine (`openai/gpt-oss-20b`) for sub-second responses.
-  **Free Local Embeddings:** Uses HuggingFace `sentence-transformers/all-MiniLM-L6-v2` locally on CPU—100% free, offline, and free of API rate limits (`429 errors`).
-  **6 Specialized Agent Tools:**
  1. `RecipeRetriever`: Semantic FAISS vector search with source citations.
  2. `WhatCanICook`: Matches & ranks recipes based on available household ingredients on hand.
  3. `SubstitutionAdvisor`: Suggests culinary ingredient replacements.
  4. `AdaptRecipe`: Dynamically rewrites recipes for dietary needs (vegan, gluten-free) or cooking time constraints.
  5. `NutritionEstimator`: Calculates calorie and macro breakdowns per serving.
  6. `ShoppingListGenerator`: Extracts structured grocery shopping lists.
-  **Web Interface & Interactive Follow-Up Chips:** Includes a clean Node.js/Express web frontend with automatic follow-up question suggestions (e.g., *"Make this vegan"*, *"Show shopping list"*).
-  **Multi-Turn Conversational Memory:** Uses LangGraph checkpointers (`session_id`) to retain context across chat turns.

---

##  Project Structure

```
recipe_rag_agent/
├── data/
│   ├── pdfs/              # Drop cookbook / recipe PDFs here
│   └── text_notes/        # .txt / .md recipe notes (58 recipes included)
├── faiss_index/           # Generated FAISS vector index (384-dim dense vectors)
├── frontend/              # Node.js / Express Web Application
│   ├── public/
│   │   ├── index.html     # Simple HTML5 Chatbot UI
│   │   ├── styles.css     # Clean CSS Stylesheet
│   │   └── app.js         # Interactive Chat logic & follow-up suggestion chips
│   ├── server.js          # Express Proxy Server (Port 3000)
│   └── package.json
├── src/
│   ├── config.py          # Central paths, retrieval Top-K, model configuration
│   ├── metadata.py        # Rule-based cuisine, diet, and time metadata tagging
│   ├── ingest.py          # PDF / text / web loaders
│   ├── chunking.py        # Recipe-aware splitting (800-char chunks)
│   ├── vectorstore.py     # FAISS build, load, and local HuggingFace embeddings
│   ├── tools.py           # LangChain tools (Retriever, Pantry Matcher, Adaptor, etc.)
│   └── agent.py           # LangGraph ReAct agent & memory checkpointer
├── api.py                 # FastAPI Python REST Backend (Port 8000)
├── main.py                # CLI Entrypoint (--build-index, --chat, --ask)
├── .env.example           # Environment Template
├── .gitignore             # Git ignore rules (protects API keys)
└── requirements.txt       # Python dependencies
```

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/wajid-65/Recipe_RAG_Agent.git
cd Recipe_RAG_Agent
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Frontend Node.js Dependencies
```bash
cd frontend
npm install
cd ..
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env` and add your free **Groq API Key** (Get one at [https://console.groq.com/keys](https://console.groq.com/keys)):
```env
GROQ_API_KEY=gsk_your_groq_api_key_here
LLM_MODEL=openai/gpt-oss-20b
```

---

##  Running the Application

### 1. Build the FAISS Vector Index (First Time Only)
Ingests all 58 recipes from `data/text_notes/` into the local FAISS vector store:
```bash
python main.py --build-index
```

### 2. Run the Web Application

#### Terminal 1 (Python FastAPI Backend):
```bash
uvicorn api:app --host 127.0.0.1 --port 8000
```

#### Terminal 2 (Node.js Express Web Server):
```bash
cd frontend
node server.js
```

#### Open Web Browser:
Go to  **[http://localhost:3000](http://localhost:3000)**

---

##  Running via Command Line (CLI Mode)

You can also run interactive chat directly in your terminal:
```bash
python main.py --chat
```

Or ask a single-shot question:
```bash
python main.py --ask "How do I make authentic Tamil Nadu Chettinad Chicken?"
```

---

## 📄 License
MIT License
