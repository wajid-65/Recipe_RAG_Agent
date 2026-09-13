"""
Unit tests for src/metadata.py — rule-based metadata tagging.
Run with: pytest tests/test_metadata.py -v
"""
import pytest
from src.metadata import (
    extract_cuisine,
    extract_diet_tags,
    extract_time_minutes,
    extract_recipe_title,
    build_metadata,
)


class TestExtractCuisine:
    def test_detects_italian(self):
        assert extract_cuisine("This is a classic Italian pasta dish.") == "Italian"

    def test_detects_indian(self):
        assert extract_cuisine("A rich Indian curry with spices.") == "Indian"

    def test_detects_mexican(self):
        assert extract_cuisine("Mexican tacos with black beans.") == "Mexican"

    def test_detects_japanese(self):
        assert extract_cuisine("Japanese ramen with miso broth.") == "Japanese"

    def test_returns_unknown_when_no_match(self):
        assert extract_cuisine("A random recipe with no cuisine clues.") == "Unknown"

    def test_case_insensitive(self):
        assert extract_cuisine("ITALIAN pasta") == "Italian"


class TestExtractDietTags:
    def test_detects_vegan(self):
        tags = extract_diet_tags("This is a vegan recipe with no animal products.")
        assert "vegan" in tags

    def test_detects_gluten_free(self):
        tags = extract_diet_tags("A gluten-free bread made with rice flour.")
        assert "gluten-free" in tags

    def test_detects_keto(self):
        tags = extract_diet_tags("Keto-friendly recipe with only 3g net carbs.")
        assert "keto" in tags

    def test_detects_multiple_tags(self):
        tags = extract_diet_tags("Vegan and gluten-free chocolate brownie recipe.")
        assert "vegan" in tags
        assert "gluten-free" in tags

    def test_returns_empty_list_when_no_match(self):
        tags = extract_diet_tags("A standard butter and flour cake recipe.")
        assert tags == []

    def test_normalizes_spaces_to_hyphens(self):
        tags = extract_diet_tags("A sugar free cake for diabetics.")
        assert "sugar-free" in tags


class TestExtractTimeMinutes:
    def test_parses_minutes(self):
        assert extract_time_minutes("Ready in 30 minutes.") == 30

    def test_parses_hours(self):
        assert extract_time_minutes("Cook for 2 hours.") == 120

    def test_parses_hours_and_minutes(self):
        assert extract_time_minutes("Takes 1 hour and 15 minutes.") == 75

    def test_returns_minus_one_when_no_time(self):
        assert extract_time_minutes("This recipe has no time information.") == -1

    def test_parses_abbreviated_min(self):
        assert extract_time_minutes("Prep: 10 min") == 10

    def test_parses_abbreviated_hr(self):
        assert extract_time_minutes("Cook: 1 hr") == 60


class TestExtractRecipeTitle:
    def test_extracts_first_line(self):
        text = "Classic Chocolate Cake\n\nIngredients..."
        assert extract_recipe_title(text) == "Classic Chocolate Cake"

    def test_strips_markdown_heading(self):
        text = "# Butter Chicken\n\nIngredients..."
        assert extract_recipe_title(text) == "Butter Chicken"

    def test_truncates_at_80_chars(self):
        long_title = "A" * 100
        result = extract_recipe_title(long_title)
        assert len(result) <= 80

    def test_skips_blank_lines(self):
        text = "\n\n\nReal Title\nStuff below"
        assert extract_recipe_title(text) == "Real Title"

    def test_returns_default_for_empty(self):
        assert extract_recipe_title("") == "Untitled Recipe"
        assert extract_recipe_title("   ") == "Untitled Recipe"


class TestBuildMetadata:
    def test_returns_all_keys(self):
        meta = build_metadata("A vegan Italian pasta recipe. Takes 30 minutes.", "pasta.md")
        assert "source" in meta
        assert "title" in meta
        assert "cuisine" in meta
        assert "diet_tags" in meta
        assert "time_minutes" in meta

    def test_source_is_preserved(self):
        meta = build_metadata("Some recipe text.", "my_recipe.txt")
        assert meta["source"] == "my_recipe.txt"

    def test_full_integration(self):
        text = """# Vegan Thai Curry
Cuisine: Thai
Time: 40 minutes
A vegan gluten-free coconut curry."""
        meta = build_metadata(text, "thai_curry.md")
        assert meta["title"] == "Vegan Thai Curry"
        assert meta["cuisine"] == "Thai"
        assert "vegan" in meta["diet_tags"]
        assert meta["time_minutes"] == 40
