"""
Lightweight, rule-based metadata tagging for recipe documents/chunks.

Why rule-based instead of an LLM call per chunk:
- Cheap and deterministic at ingestion time (no API cost per chunk)
- Good enough for filtering (cuisine / diet) at retrieval time
- Can be swapped for an LLM-based tagger later without changing the
  rest of the pipeline (see `llm_tag_chunk` stub at the bottom).
"""
import re
from typing import Dict, List

from src.config import KNOWN_CUISINES, KNOWN_DIET_TAGS


def extract_cuisine(text: str) -> str:
    text_lower = text.lower()
    for cuisine in KNOWN_CUISINES:
        if cuisine in text_lower:
            return cuisine.title()
    return "Unknown"


def extract_diet_tags(text: str) -> List[str]:
    text_lower = text.lower()
    found = set()
    for tag in KNOWN_DIET_TAGS:
        if tag in text_lower:
            found.add(tag.replace(" ", "-"))
    return sorted(found)


def extract_time_minutes(text: str) -> int:
    """
    Best-effort extraction of total time in minutes from phrases like:
    '30 minutes', '1 hour', '1 hr 15 min', '45 mins'
    Returns -1 if nothing found (treated as 'unknown' at filter time).
    """
    text_lower = text.lower()

    hours = 0
    minutes = 0

    hr_match = re.search(r"(\d+)\s*(?:hours?|hrs?)", text_lower)
    if hr_match:
        hours = int(hr_match.group(1))

    min_match = re.search(r"(\d+)\s*(?:minutes?|mins?)", text_lower)
    if min_match:
        minutes = int(min_match.group(1))

    total = hours * 60 + minutes
    return total if total > 0 else -1


def extract_recipe_title(text: str) -> str:
    """
    Heuristic: first non-empty line, stripped of markdown symbols,
    truncated to a reasonable title length.
    """
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line:
            return line[:80]
    return "Untitled Recipe"


def build_metadata(text: str, source: str) -> Dict:
    """
    Build the metadata dict attached to each chunk before indexing.
    """
    return {
        "source": source,
        "title": extract_recipe_title(text),
        "cuisine": extract_cuisine(text),
        "diet_tags": extract_diet_tags(text),
        "time_minutes": extract_time_minutes(text),
    }


def llm_tag_chunk(llm, text: str) -> Dict:
    """
    Optional upgrade path: use the LLM to tag chunks more accurately
    (handles cases the rule-based tagger misses, e.g. cuisines not in
    KNOWN_CUISINES, or implicit diet suitability like "no dairy used").

    Not called by default (adds cost/latency at ingestion time).
    Wire this into vectorstore.py's `tag_documents` if you want higher
    tagging accuracy and are OK with the extra LLM calls.
    """
    prompt = f"""Extract structured metadata from this recipe text.
Return ONLY valid JSON with keys: cuisine (string), diet_tags (list of strings),
time_minutes (integer, -1 if unknown).

Text:
{text[:1500]}
"""
    response = llm.invoke(prompt)
    import json
    try:
        return json.loads(response.content)
    except Exception:
        return {"cuisine": "Unknown", "diet_tags": [], "time_minutes": -1}
