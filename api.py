"""
FastAPI Backend for Recipe RAG Agent
"""
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Ensure project root is in sys.path
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.vectorstore import load_vectorstore
from src.agent import build_agent, ask
from src.config import LLM_MODEL

app = FastAPI(
    title="Recipe RAG Agent API",
    description="Groq-powered Recipe RAG Chatbot Backend with LangChain and LangGraph",
    version="1.0.0"
)

# Enable CORS for Node.js Express frontend or direct web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_vectorstore = None
_agent = None

def get_agent_instance():
    global _vectorstore, _agent
    if _agent is None:
        _vectorstore = load_vectorstore()
        if _vectorstore is None:
            raise HTTPException(
                status_code=500,
                detail="FAISS vector store index not found. Run 'python main.py --build-index' first."
            )
        _agent = build_agent(_vectorstore)
    return _agent


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    answer: str
    session_id: str


@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Recipe RAG Agent API",
        "llm_provider": "Groq",
        "model": LLM_MODEL
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    
    agent = get_agent_instance()
    try:
        answer_text = ask(agent, req.message.strip(), session_id=req.session_id)
        return ChatResponse(answer=answer_text, session_id=req.session_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
