"""
FAISS vector store: build, save, load, incrementally update, and
run metadata-filtered similarity search.
"""
import os
from typing import List, Optional, Dict, Any

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings

from src.config import FAISS_INDEX_PATH, RETRIEVER_TOP_K, EMBEDDING_MODEL


_embeddings_instance = None


def get_embeddings() -> HuggingFaceEmbeddings:
    global _embeddings_instance
    if _embeddings_instance is None:
        _embeddings_instance = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return _embeddings_instance



def build_vectorstore(chunks: List[Document], save_path: str = FAISS_INDEX_PATH) -> FAISS:
    """
    Builds a new FAISS index from scratch using HuggingFace local embeddings
    and saves it to disk. Fast and offline.
    """
    import logging
    logger = logging.getLogger(__name__)

    total = len(chunks)
    logger.info(f"Building FAISS vector store with {total} chunks...")
    print(f"[vectorstore] Generating local embeddings for {total} chunks...")

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(save_path)
    logger.info(f"Vector store built and saved to {save_path}")
    print(f"[vectorstore] Built and saved FAISS index at '{save_path}' ({total} chunks)")
    return vectorstore




def load_vectorstore(load_path: str = FAISS_INDEX_PATH) -> Optional[FAISS]:
    """
    Loads an existing FAISS index from disk. Returns None if not found.
    """
    index_file = os.path.join(load_path, "index.faiss")
    if not os.path.isfile(index_file):
        print(f"[vectorstore] No existing index found at '{load_path}'")
        return None

    embeddings = get_embeddings()
    vectorstore = FAISS.load_local(
        load_path, embeddings, allow_dangerous_deserialization=True
    )
    print(f"[vectorstore] Loaded FAISS index from '{load_path}'")
    return vectorstore


def add_documents(vectorstore: FAISS, new_chunks: List[Document], save_path: str = FAISS_INDEX_PATH) -> FAISS:
    """
    Incrementally adds new chunks to an existing index (e.g. when the
    user uploads a new recipe file without re-indexing everything).
    """
    vectorstore.add_documents(new_chunks)
    vectorstore.save_local(save_path)
    print(f"[vectorstore] Added {len(new_chunks)} new chunks and re-saved index")
    return vectorstore


def get_or_build_vectorstore(chunks: List[Document], save_path: str = FAISS_INDEX_PATH) -> FAISS:
    """
    Convenience entrypoint: loads the index if it exists, otherwise
    builds a fresh one from the given chunks.
    """
    vectorstore = load_vectorstore(save_path)
    if vectorstore is None:
        vectorstore = build_vectorstore(chunks, save_path)
    return vectorstore


def filtered_retrieve(
    vectorstore: FAISS,
    query: str,
    k: int = RETRIEVER_TOP_K,
    cuisine: Optional[str] = None,
    diet_tag: Optional[str] = None,
    max_time_minutes: Optional[int] = None,
) -> List[Document]:
    """
    Similarity search with post-hoc metadata filtering.

    Note: FAISS's native similarity_search doesn't support arbitrary
    metadata filters as well as some other vector DBs, so we
    over-fetch (k * 4) and filter in Python. Good enough at this
    document scale; swap for a metadata-filtering vector DB (e.g.
    Chroma, Qdrant) if the corpus grows very large.
    """
    fetch_k = max(k * 4, 20)
    candidates = vectorstore.similarity_search(query, k=fetch_k)

    def matches(doc: Document) -> bool:
        meta = doc.metadata
        if cuisine and meta.get("cuisine", "").lower() != cuisine.lower():
            return False
        if diet_tag and diet_tag.lower() not in [t.lower() for t in meta.get("diet_tags", [])]:
            return False
        if max_time_minutes is not None:
            t = meta.get("time_minutes", -1)
            if t != -1 and t > max_time_minutes:
                return False
        return True

    filtered = [d for d in candidates if matches(d)]

    # If filters were too strict and produced nothing, fall back to
    # unfiltered top-k rather than returning an empty context.
    if not filtered:
        return candidates[:k]

    return filtered[:k]


if __name__ == "__main__":
    from src.ingest import load_all_documents
    from src.chunking import chunk_documents

    docs = load_all_documents()
    chunks = chunk_documents(docs)
    vs = get_or_build_vectorstore(chunks)

    results = filtered_retrieve(vs, "chocolate cake", diet_tag="sugar-free")
    for r in results:
        print(r.metadata.get("title"), "|", r.metadata.get("cuisine"), "|", r.metadata.get("diet_tags"))
