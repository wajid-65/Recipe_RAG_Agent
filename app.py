"""
Recipe RAG Agent — Streamlit Web UI
Run with: streamlit run app.py

Features:
- Conversational chat with multi-turn memory (one session per browser tab)
- File uploader: drag-and-drop PDFs or text/markdown recipe files to expand
  the knowledge base live without restarting
- HTML recipe visualizer: generates and embeds the styled recipe card inline
- Sidebar: shows agent tools, knowledge-base stats, and quick example prompts
"""

import os
import json
import tempfile
import time
import streamlit as st

# ── Page config (must be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="🍽️ Recipe RAG Agent",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Dark gradient background */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    min-height: 100vh;
}

/* Main container */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* Header */
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, #f9a825, #ff6b35, #e91e8c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0;
    line-height: 1.2;
}

.hero-subtitle {
    color: rgba(255,255,255,0.6);
    font-size: 1rem;
    margin-top: 0.3rem;
    margin-bottom: 1.5rem;
}

/* Chat messages */
.stChatMessage {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important;
    backdrop-filter: blur(10px);
    margin-bottom: 0.75rem;
}

/* User message accent */
[data-testid="stChatMessageContent"] {
    color: rgba(255,255,255,0.92) !important;
}

/* Chat input */
.stChatInputContainer {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(249,168,37,0.4) !important;
    border-radius: 16px !important;
    backdrop-filter: blur(10px);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(15,12,41,0.95) 0%, rgba(48,43,99,0.95) 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}

[data-testid="stSidebar"] .stMarkdown {
    color: rgba(255,255,255,0.85) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #f9a825, #ff6b35) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(249,168,37,0.4) !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05) !important;
    border: 1px dashed rgba(249,168,37,0.5) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 0.75rem 1rem !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
    color: rgba(255,255,255,0.85) !important;
}

/* Info / success / error boxes */
.stAlert {
    border-radius: 12px !important;
}

/* Recipe HTML card wrapper */
.recipe-html-wrapper {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 1rem;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #f9a825 !important;
}
</style>
""", unsafe_allow_html=True)


# ── Lazy imports (avoid requiring API key at import time) ────────────────────
@st.cache_resource(show_spinner=False)
def _load_vectorstore():
    """Load existing FAISS index. Cached so it's only read once per session."""
    from src.vectorstore import load_vectorstore
    return load_vectorstore()


@st.cache_resource(show_spinner=False)
def _build_agent(_vectorstore):
    """Build the LangGraph agent. Cached per vectorstore instance."""
    from src.agent import build_agent
    return build_agent(_vectorstore)


def get_vectorstore():
    """Return vectorstore from session state or cache."""
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = _load_vectorstore()
    return st.session_state.vectorstore


def get_agent():
    """Return agent from session state or build from vectorstore."""
    vs = get_vectorstore()
    if vs is None:
        return None
    if "agent" not in st.session_state:
        with st.spinner("🤖 Loading Recipe Agent…"):
            st.session_state.agent = _build_agent(vs)
    return st.session_state.agent


def get_session_id() -> str:
    """Unique session ID per browser tab."""
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id


def ingest_uploaded_file(uploaded_file) -> int:
    """Save uploaded file to a temp location, chunk it, and add to index."""
    from src.chunking import chunk_documents
    from src.vectorstore import add_documents
    from langchain_core.documents import Document

    suffix = os.path.splitext(uploaded_file.name)[1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name

    try:
        docs = []
        if suffix == ".pdf":
            from langchain_community.document_loaders import PyPDFLoader
            loaded = PyPDFLoader(tmp_path).load()
            for d in loaded:
                d.metadata["source"] = uploaded_file.name
            docs.extend(loaded)
        elif suffix in (".txt", ".md"):
            from langchain_community.document_loaders import TextLoader
            loaded = TextLoader(tmp_path, encoding="utf-8").load()
            for d in loaded:
                d.metadata["source"] = uploaded_file.name
            docs.extend(loaded)
        else:
            st.warning(f"Unsupported file type: {suffix}")
            return 0

        if not docs:
            return 0

        chunks = chunk_documents(docs)
        vs = get_vectorstore()
        add_documents(vs, chunks)

        # Invalidate agent cache so it uses the updated vectorstore
        if "agent" in st.session_state:
            del st.session_state["agent"]

        return len(chunks)
    finally:
        os.unlink(tmp_path)


def render_html_card(agent_answer: str) -> str:
    """Generate and return the HTML visualization as a string."""
    from src.tools import nutrition_tool, shopping_list_tool
    from src.visualize import render_recipe_html

    nutrition = nutrition_tool(agent_answer)
    shopping = shopping_list_tool(agent_answer)
    path = render_recipe_html(
        agent_answer,
        nutrition_json=nutrition,
        shopping_json=shopping,
        filename=f"recipe_{int(time.time())}.html",
    )
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍽️ Recipe RAG Agent")
    st.markdown("---")

    # Knowledge base stats
    st.markdown("### 📚 Knowledge Base")
    vs = get_vectorstore()
    if vs is not None:
        try:
            n_vectors = vs.index.ntotal
            st.metric("Indexed Recipe Chunks", n_vectors)
        except Exception:
            st.info("Index loaded")
    else:
        st.warning("No index found. Build it first.")
        if st.button("⚙️ Build Index from data/ folder"):
            with st.spinner("Building index…"):
                try:
                    from src.ingest import load_all_documents
                    from src.chunking import chunk_documents
                    from src.vectorstore import get_or_build_vectorstore
                    docs = load_all_documents()
                    if docs:
                        chunks = chunk_documents(docs)
                        st.session_state.vectorstore = get_or_build_vectorstore(chunks)
                        if "agent" in st.session_state:
                            del st.session_state["agent"]
                        st.success(f"✅ Indexed {len(chunks)} chunks!")
                        st.rerun()
                    else:
                        st.error("No documents found under data/")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("---")

    # File uploader
    st.markdown("### 📂 Upload Recipe Files")
    uploaded = st.file_uploader(
        "Drop PDFs or .md/.txt recipe files here to add them to the knowledge base.",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    if uploaded:
        if st.button("➕ Ingest Uploaded Files"):
            total_chunks = 0
            for f in uploaded:
                with st.spinner(f"Ingesting {f.name}…"):
                    try:
                        n = ingest_uploaded_file(f)
                        total_chunks += n
                        st.success(f"✅ {f.name}: {n} chunks added")
                    except Exception as e:
                        st.error(f"❌ {f.name}: {e}")
            if total_chunks:
                st.success(f"Added {total_chunks} total chunks to the index!")
                st.rerun()

    st.markdown("---")

    # Example prompts
    st.markdown("### 💡 Example Questions")
    examples = [
        "How do I make a sugar-free chocolate cake?",
        "I have tofu, broccoli and coconut milk. What can I cook?",
        "Give me a vegan version of butter chicken.",
        "What's a quick gluten-free dinner under 30 minutes?",
        "How can I substitute eggs in a cake recipe?",
        "What are the nutrition facts for miso ramen?",
        "Make the carbonara recipe dairy-free.",
    ]
    for ex in examples:
        if st.button(ex, key=f"ex_{ex[:20]}", use_container_width=True):
            st.session_state.pending_input = ex
            st.rerun()

    st.markdown("---")

    # Tools info
    with st.expander("🔧 Agent Tools"):
        st.markdown("""
| Tool | Purpose |
|------|---------|
| RecipeRetriever | Search knowledge base |
| WhatCanICook | Match available ingredients |
| SubstitutionAdvisor | Ingredient swaps |
| AdaptRecipe | Diet / time / cuisine changes |
| NutritionEstimator | Per-serving nutrition |
| ShoppingListGenerator | Shopping checklist |
""")

    # Clear chat
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        if "session_id" in st.session_state:
            del st.session_state["session_id"]
        st.rerun()


# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown('<p class="hero-title">🍽️ Recipe RAG Agent</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Ask anything about recipes — personalized, adapted, and grounded in your knowledge base.</p>', unsafe_allow_html=True)

# Show / hide HTML visualization toggle
col1, col2 = st.columns([4, 1])
with col2:
    show_html = st.toggle("🎨 Show Recipe Card", value=False, help="Render a styled HTML recipe card for the last answer")

# ── Chat history ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🍽️"):
        st.markdown(msg["content"])

# ── Process example-button shortcut ──────────────────────────────────────────
prompt = None
if "pending_input" in st.session_state:
    prompt = st.session_state.pop("pending_input")

# ── Chat input ────────────────────────────────────────────────────────────────
chat_prompt = st.chat_input("Ask about a recipe, ingredients, dietary needs…")
if chat_prompt:
    prompt = chat_prompt

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    agent = get_agent()

    if agent is None:
        with st.chat_message("assistant", avatar="🍽️"):
            st.error("❌ No index loaded. Build the index first using the sidebar button.")
    else:
        with st.chat_message("assistant", avatar="🍽️"):
            with st.spinner("🍳 Cooking up an answer…"):
                try:
                    from src.agent import ask
                    answer = ask(agent, prompt, session_id=get_session_id())

                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})

                    # Optionally render HTML card
                    if show_html:
                        with st.spinner("🎨 Rendering recipe card…"):
                            try:
                                html_content = render_html_card(answer)
                                with st.expander("📄 Styled Recipe Card", expanded=True):
                                    st.components.v1.html(html_content, height=700, scrolling=True)
                            except Exception as e:
                                st.warning(f"Could not render HTML card: {e}")

                except Exception as e:
                    err = str(e)
                    if "RESOURCE_EXHAUSTED" in err or "429" in err:
                        st.error(
                            "⚠️ **Gemini API quota exceeded** (free-tier rate limit hit).\n\n"
                            "Wait a moment and try again, or enable billing on your "
                            "[Google AI Studio project](https://ai.dev/rate-limit) for higher limits."
                        )
                    elif "API_KEY_INVALID" in err or "UNAUTHENTICATED" in err or "PERMISSION_DENIED" in err:
                        st.error(
                            "🔑 **Invalid API Key.**\n\n"
                            "Open `.env` and paste a valid `GOOGLE_API_KEY` from "
                            "[aistudio.google.com/apikey](https://aistudio.google.com/apikey), "
                            "then restart the app."
                        )
                    else:
                        st.error(f"❌ Error: {err}")

# ── Empty state ───────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
<div style="text-align:center; padding: 3rem 1rem; color: rgba(255,255,255,0.35);">
    <div style="font-size: 4rem;">🍳</div>
    <div style="font-size: 1.1rem; margin-top: 1rem;">Ask me anything about recipes!</div>
    <div style="font-size: 0.9rem; margin-top: 0.5rem;">Try one of the example prompts in the sidebar →</div>
</div>
""", unsafe_allow_html=True)
