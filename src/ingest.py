"""
Document ingestion: loads recipes from PDFs, plain text/markdown files,
and web URLs into a unified list of LangChain Document objects.
"""
import os
from typing import List

# Import config FIRST -- it sets the USER_AGENT env var, and some
# LangChain loader modules check that env var at import time.
from src.config import PDF_DIR, TEXT_DIR, URLS_FILE

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)


def load_pdfs(pdf_dir: str = PDF_DIR) -> List[Document]:
    docs = []
    if not os.path.isdir(pdf_dir):
        return docs

    for fname in os.listdir(pdf_dir):
        if fname.lower().endswith(".pdf"):
            path = os.path.join(pdf_dir, fname)
            try:
                loaded = PyPDFLoader(path).load()
                for d in loaded:
                    d.metadata["source"] = fname
                docs.extend(loaded)
                print(f"[ingest] Loaded PDF: {fname} ({len(loaded)} pages)")
            except Exception as e:
                print(f"[ingest] Failed to load {fname}: {e}")
    return docs


def load_text_notes(text_dir: str = TEXT_DIR) -> List[Document]:
    """
    Loads .txt and .md recipe notes. Each file is treated as one
    document (chunking happens later in chunking.py).
    """
    docs = []
    if not os.path.isdir(text_dir):
        return docs

    for fname in os.listdir(text_dir):
        if fname.lower().endswith((".txt", ".md")):
            path = os.path.join(text_dir, fname)
            try:
                loaded = TextLoader(path, encoding="utf-8").load()
                for d in loaded:
                    d.metadata["source"] = fname
                docs.extend(loaded)
                print(f"[ingest] Loaded text note: {fname}")
            except Exception as e:
                print(f"[ingest] Failed to load {fname}: {e}")
    return docs


def load_urls(urls_file: str = URLS_FILE) -> List[Document]:
    """
    Loads recipe blog pages from a newline-separated list of URLs.
    """
    docs = []
    if not os.path.isfile(urls_file):
        return docs

    with open(urls_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not urls:
        return docs

    try:
        loaded = WebBaseLoader(urls).load()
        for d in loaded:
            d.metadata["source"] = d.metadata.get("source", "web")
        docs.extend(loaded)
        print(f"[ingest] Loaded {len(loaded)} web page(s) from urls.txt")
    except Exception as e:
        print(f"[ingest] Failed to load URLs: {e}")

    return docs


def load_all_documents() -> List[Document]:
    """
    Master ingestion entrypoint. Aggregates all supported sources.
    Extend this with more loaders (e.g. Docx2txtLoader, CSVLoader)
    as new source types are added.
    """
    docs = []
    docs.extend(load_pdfs())
    docs.extend(load_text_notes())
    docs.extend(load_urls())

    if not docs:
        print(
            "[ingest] WARNING: No documents found. "
            "Add files to data/pdfs/, data/text_notes/, or URLs to data/urls.txt."
        )
    else:
        print(f"[ingest] Total documents loaded: {len(docs)}")

    return docs


if __name__ == "__main__":
    documents = load_all_documents()
    for d in documents[:3]:
        print("---")
        print(d.metadata)
        print(d.page_content[:200])
