"""
Recipe-aware chunking.

Plain fixed-size character splitting tends to cut a recipe's
ingredients list away from its instructions. This module:

1. First tries to split each source document into per-recipe blocks,
   using common recipe heading patterns (markdown headers, "Recipe:",
   all-caps title lines, or blank-line-separated blocks).
2. Falls back to RecursiveCharacterTextSplitter for any block that is
   still too large after step 1 (e.g. a whole cookbook chapter).
3. Tags every resulting chunk with metadata (cuisine, diet, time,
   title, source) via metadata.py so retrieval can filter on it.
"""
import re
from typing import List

from langchain_core.documents import Document

try:
    # Newer LangChain versions ship text splitters in this separate package
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    # Older LangChain versions expose it from the main package
    from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.config import CHUNK_SIZE, CHUNK_OVERLAP
from src.metadata import build_metadata

# Patterns that typically mark the start of a NEW RECIPE (not a subsection
# within one recipe). Only top-level (#) headers count as boundaries --
# "## Ingredients" / "## Instructions" are subsections of the same recipe
# and must stay grouped with it, which is the whole point of this splitter.
RECIPE_BOUNDARY_PATTERN = re.compile(
    r"(?:\n#\s+.+\n)"               # top-level markdown header (single #)
    r"|(?:\nRecipe\s*:.+\n)"        # "Recipe: <name>"
    r"|(?:\n[A-Z][A-Z\s]{4,}\n)",   # ALL CAPS title lines
    re.MULTILINE,
)


def split_into_recipe_blocks(text: str) -> List[str]:
    """
    Splits raw text into per-recipe blocks using heading heuristics.
    If no clear boundaries are found, returns the text as a single block.
    """
    matches = list(RECIPE_BOUNDARY_PATTERN.finditer(text))
    if not matches:
        return [text]

    blocks = []
    start_positions = [m.start() for m in matches]

    # Keep any preamble before the first detected boundary
    if start_positions[0] > 0:
        preamble = text[: start_positions[0]].strip()
        if preamble:
            blocks.append(preamble)

    for i, start in enumerate(start_positions):
        end = start_positions[i + 1] if i + 1 < len(start_positions) else len(text)
        block = text[start:end].strip()
        if block:
            blocks.append(block)

    return blocks


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Full pipeline: recipe-block split -> size-based fallback split ->
    metadata tagging. Returns a flat list of chunked, tagged Documents
    ready for embedding.
    """
    fallback_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " "],
    )

    final_chunks: List[Document] = []

    for doc in documents:
        source = doc.metadata.get("source", "unknown")
        recipe_blocks = split_into_recipe_blocks(doc.page_content)

        for block in recipe_blocks:
            if len(block) <= CHUNK_SIZE * 1.5:
                # Block is a reasonable single chunk -- keep it whole
                # so ingredients + instructions stay together.
                sub_chunks = [block]
            else:
                # Too large (e.g. a whole chapter) -- fall back to
                # character-based splitting.
                sub_chunks = fallback_splitter.split_text(block)

            for chunk_text in sub_chunks:
                meta = build_metadata(chunk_text, source)
                meta.update({k: v for k, v in doc.metadata.items() if k not in meta})
                final_chunks.append(Document(page_content=chunk_text, metadata=meta))

    print(f"[chunking] Produced {len(final_chunks)} chunks from {len(documents)} documents")
    return final_chunks


if __name__ == "__main__":
    from src.ingest import load_all_documents

    docs = load_all_documents()
    chunks = chunk_documents(docs)
    for c in chunks[:3]:
        print("---")
        print(c.metadata)
        print(c.page_content[:200])
