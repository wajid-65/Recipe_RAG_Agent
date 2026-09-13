"""
Recipe RAG Agent -- CLI entrypoint.

Usage:
    python main.py --build-index          # ingest + chunk + index
    python main.py --chat                 # interactive Q&A
    python main.py --ask "your question"  # single question, prints answer
    python main.py --ask "..." --html     # also renders an HTML artifact
"""
import argparse
import io
import sys
import time
import uuid

# Force UTF-8 stdout/stderr on Windows to prevent UnicodeEncodeError
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


from src.ingest import load_all_documents
from src.chunking import chunk_documents
from src.vectorstore import build_vectorstore, load_vectorstore, add_documents
# NOTE: src.agent / src.tools are imported lazily inside run_chat() and
# run_single_question() below, NOT at module level. Those modules create a
# Gemini client, so importing them eagerly would require GOOGLE_API_KEY to
# be set even for --build-index, which only needs embeddings.


def build_index():
    docs = load_all_documents()
    if not docs:
        print("No documents found -- add files under data/ first.")
        return
    chunks = chunk_documents(docs)
    # Always force a fresh rebuild so newly added recipe files are included.
    # (get_or_build_vectorstore would silently reuse the old index if it exists)
    build_vectorstore(chunks)
    print(f"Index built successfully with {len(chunks)} recipe chunks!")


def run_chat():
    from src.agent import build_agent, ask

    vectorstore = load_vectorstore()
    if vectorstore is None:
        print("No index found. Run: python main.py --build-index")
        return

    agent = build_agent(vectorstore)
    # Use a unique session ID per run so we never accidentally load
    # corrupted/incomplete history from a previously interrupted session.
    session_id = f"cli-{uuid.uuid4().hex[:8]}"
    print("Recipe RAG Agent ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue
        try:
            answer = ask(agent, user_input, session_id=session_id)
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                print(
                    "\n[Gemini API quota exceeded -- wait for reset, or enable "
                    "billing on your Google AI Studio project. Check usage at "
                    "https://ai.dev/rate-limit]\n"
                )
                continue
            raise
        print(f"\nAgent: {answer}\n")


def run_single_question(question: str, make_html: bool = False):
    from src.agent import build_agent, ask
    from src.tools import nutrition_tool, shopping_list_tool
    from src.visualize import render_recipe_html

    vectorstore = load_vectorstore()
    if vectorstore is None:
        print("No index found. Run: python main.py --build-index")
        return

    agent = build_agent(vectorstore)
    try:
        answer = ask(agent, question, session_id="single-shot")
    except Exception as e:
        if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
            print(
                "\nGemini API quota exceeded (free-tier daily/rate limit hit).\n"
                "This is not a code error -- either wait for the quota to reset, "
                "or enable billing on your Google AI Studio project for higher limits.\n"
                "Check current usage at: https://ai.dev/rate-limit\n"
            )
            return
        raise
    print(answer)

    if make_html:
        # Best-effort: also produce standalone nutrition/shopping JSON
        # for the visualizer, generated directly from the answer text.
        nutrition = nutrition_tool(answer)
        shopping = shopping_list_tool(answer)
        path = render_recipe_html(answer, nutrition_json=nutrition, shopping_json=shopping)
        print(f"\nHTML artifact written to: {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recipe RAG Agent")
    parser.add_argument("--build-index", action="store_true", help="Ingest documents and build FAISS index")
    parser.add_argument("--chat", action="store_true", help="Start interactive chat session")
    parser.add_argument("--ask", type=str, help="Ask a single question")
    parser.add_argument("--html", action="store_true", help="Also render an HTML visualization (use with --ask)")

    args = parser.parse_args()

    if args.build_index:
        build_index()
    elif args.chat:
        run_chat()
    elif args.ask:
        run_single_question(args.ask, make_html=args.html)
    else:
        parser.print_help()
