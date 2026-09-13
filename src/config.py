"""
Central configuration for the Recipe RAG Agent.
"""
import os
from dotenv import load_dotenv

# Load .env explicitly from the project root (this file's parent directory),
# not the current working directory -- load_dotenv() with no args only
# searches cwd upward, which silently finds nothing if you run
# `python main.py` from a different folder or via an IDE run config.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ENV_PATH = os.path.join(_PROJECT_ROOT, ".env")
load_dotenv(dotenv_path=_ENV_PATH)

# Silences LangChain's WebBaseLoader warning about missing USER_AGENT
os.environ.setdefault("USER_AGENT", "recipe-rag-agent/1.0")

# --- API ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_DIR = os.path.join(DATA_DIR, "pdfs")
TEXT_DIR = os.path.join(DATA_DIR, "text_notes")
URLS_FILE = os.path.join(DATA_DIR, "urls.txt")
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# --- Chunking ---
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# --- Retrieval ---
RETRIEVER_TOP_K = 2

# --- LLM & Embeddings ---
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")
LLM_TEMPERATURE = 0.3
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"



# --- Known tag vocab (used for lightweight metadata tagging) ---
KNOWN_CUISINES = [
    "italian", "indian", "chinese", "mexican", "thai", "french",
    "japanese", "mediterranean", "american", "korean", "middle eastern",
    "vietnamese", "greek", "spanish", "tamil nadu", "tamil", "south indian",
    "british", "english"
]

KNOWN_DIET_TAGS = [
    "vegan", "vegetarian", "gluten-free", "gluten free", "sugar-free",
    "sugar free", "keto", "low-carb", "low carb", "dairy-free",
    "dairy free", "nut-free", "nut free", "paleo", "high-protein"
]
