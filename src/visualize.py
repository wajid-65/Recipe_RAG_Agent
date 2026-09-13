"""
Renders a recipe response as a self-contained HTML page with:
- a numbered step tracker
- a shopping list checklist
- a nutrition facts card
- substitution callouts

This satisfies the "visualize cooking guidance" requirement without
needing a frontend framework -- just open the generated .html file
in a browser.
"""
import json
import os
import re
from typing import List, Dict, Optional

from src.config import OUTPUT_DIR

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; background:#faf7f2; color:#2b2b2b; max-width:760px; margin:40px auto; padding:0 20px; }}
  h1 {{ color:#b5502e; }}
  .card {{ background:#fff; border-radius:12px; padding:20px 24px; margin-bottom:20px; box-shadow:0 1px 4px rgba(0,0,0,0.08); }}
  .adaptations {{ background:#fff6ec; border-left:4px solid #e8a13a; }}
  .step {{ display:flex; gap:12px; margin-bottom:14px; align-items:flex-start; }}
  .step-num {{ background:#b5502e; color:#fff; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0; }}
  ul.shopping {{ list-style:none; padding:0; }}
  ul.shopping li {{ padding:8px 0; border-bottom:1px solid #eee; display:flex; justify-content:space-between; }}
  ul.shopping li::before {{ content:"\\2610"; margin-right:10px; color:#b5502e; }}
  .nutrition-grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:12px; text-align:center; }}
  .nutrition-grid div {{ background:#fff6ec; border-radius:8px; padding:10px; }}
  .nutrition-grid .value {{ font-size:1.3em; font-weight:bold; color:#b5502e; }}
  .sources {{ font-size:0.85em; color:#777; }}
</style>
</head>
<body>
<h1>{title}</h1>

{adaptations_block}

<div class="card">
  <h2>Ingredients</h2>
  <p>{ingredients_html}</p>
</div>

<div class="card">
  <h2>Step-by-Step Instructions</h2>
  {steps_html}
</div>

{nutrition_block}

{shopping_block}

<p class="sources">{sources}</p>
</body>
</html>
"""


def _parse_agent_markdown(agent_output: str) -> Dict:
    """
    Best-effort parse of the agent's structured markdown answer into
    sections, so we can drop them into the HTML template.
    """
    sections = {
        "title": "Recipe",
        "adaptations": "",
        "ingredients": "",
        "steps": "",
        "sources": "",
    }

    patterns = {
        "title": r"\*\*Recipe Name:\*\*(.*?)(?=\*\*|$)",
        "adaptations": r"\*\*Adaptations Made:\*\*(.*?)(?=\*\*|$)",
        "ingredients": r"\*\*Ingredients:\*\*(.*?)(?=\*\*|$)",
        "steps": r"\*\*Step-by-Step Instructions:\*\*(.*?)(?=\*\*Nutritional|\*\*Shopping|\*\*Sources|$)",
        "sources": r"\*\*Sources:\*\*(.*?)$",
    }

    for key, pattern in patterns.items():
        m = re.search(pattern, agent_output, re.DOTALL)
        if m:
            sections[key] = m.group(1).strip()

    if not sections["title"] or sections["title"] == "Recipe":
        sections["title"] = "Recipe"

    return sections


def render_recipe_html(
    agent_output: str,
    nutrition_json: Optional[str] = None,
    shopping_json: Optional[str] = None,
    filename: str = "recipe_output.html",
) -> str:
    """
    Builds the HTML file and writes it to OUTPUT_DIR. Returns the path.
    """
    parsed = _parse_agent_markdown(agent_output)

    adaptations_block = ""
    if parsed["adaptations"] and parsed["adaptations"].lower() not in ("none", "n/a", ""):
        adaptations_block = f"""<div class="card adaptations">
  <h2>Adaptations Made</h2>
  <p>{parsed['adaptations']}</p>
</div>"""

    steps_html = ""
    step_lines = [s.strip() for s in re.split(r"\n?\d+\.\s+", parsed["steps"]) if s.strip()]
    if not step_lines:
        steps_html = f"<p>{parsed['steps'] or 'No steps available.'}</p>"
    else:
        for i, step in enumerate(step_lines, 1):
            steps_html += f"""<div class="step"><div class="step-num">{i}</div><div>{step}</div></div>\n"""

    nutrition_block = ""
    if nutrition_json:
        try:
            n = json.loads(nutrition_json)
            nutrition_block = f"""<div class="card">
  <h2>Nutrition Facts (per serving)</h2>
  <div class="nutrition-grid">
    <div><div class="value">{n.get('calories', '?')}</div>Calories</div>
    <div><div class="value">{n.get('protein_g', '?')}g</div>Protein</div>
    <div><div class="value">{n.get('carbs_g', '?')}g</div>Carbs</div>
    <div><div class="value">{n.get('fat_g', '?')}g</div>Fat</div>
  </div>
  <p style="font-size:0.85em;color:#777;margin-top:10px;">{n.get('note', '')}</p>
</div>"""
        except Exception:
            pass

    shopping_block = ""
    if shopping_json:
        try:
            items = json.loads(shopping_json)
            list_items = "".join(
                f"<li><span>{it.get('item','')}</span><span>{it.get('quantity','')}</span></li>"
                for it in items
            )
            shopping_block = f"""<div class="card">
  <h2>Shopping List</h2>
  <ul class="shopping">{list_items}</ul>
</div>"""
        except Exception:
            pass

    html = HTML_TEMPLATE.format(
        title=parsed["title"],
        adaptations_block=adaptations_block,
        ingredients_html=parsed["ingredients"] or "N/A",
        steps_html=steps_html,
        nutrition_block=nutrition_block,
        shopping_block=shopping_block,
        sources=parsed["sources"],
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[visualize] Wrote {out_path}")
    return out_path
