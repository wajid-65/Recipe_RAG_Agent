"""
Unit tests for src/chunking.py — recipe-aware document chunking.
Run with: pytest tests/test_chunking.py -v
"""
import pytest
from langchain_core.documents import Document
from src.chunking import split_into_recipe_blocks, chunk_documents


SINGLE_RECIPE = """# Classic Chocolate Cake

Cuisine: American
Time: 45 minutes

## Ingredients
- 2 cups flour
- 2 cups sugar

## Instructions
1. Mix dry ingredients.
2. Add wet ingredients.
3. Bake at 350F.
"""

TWO_RECIPES = """# Recipe One

This is the first recipe.
Ingredients: eggs, flour.
Instructions: Mix and cook.

# Recipe Two

This is the second recipe.
Ingredients: tomatoes, pasta.
Instructions: Boil and mix.
"""

LARGE_RECIPE = "This is a very long recipe text. " * 100  # > CHUNK_SIZE


class TestSplitIntoRecipeBlocks:
    def test_single_recipe_returns_one_block(self):
        blocks = split_into_recipe_blocks(SINGLE_RECIPE)
        assert len(blocks) == 1

    def test_two_recipes_returns_two_blocks(self):
        blocks = split_into_recipe_blocks(TWO_RECIPES)
        assert len(blocks) == 2

    def test_blocks_are_non_empty_strings(self):
        blocks = split_into_recipe_blocks(SINGLE_RECIPE)
        for block in blocks:
            assert isinstance(block, str)
            assert len(block.strip()) > 0

    def test_no_boundaries_returns_original_as_single_block(self):
        text = "Just some plain text with no recipe headers."
        blocks = split_into_recipe_blocks(text)
        assert len(blocks) == 1
        assert blocks[0] == text

    def test_recipe_colon_pattern_detected(self):
        text = "\nRecipe: Butter Chicken\nIngredients...\n\nRecipe: Pasta\nIngredients..."
        blocks = split_into_recipe_blocks(text)
        assert len(blocks) >= 2


class TestChunkDocuments:
    def test_returns_list_of_documents(self):
        docs = [Document(page_content=SINGLE_RECIPE, metadata={"source": "test.md"})]
        chunks = chunk_documents(docs)
        assert isinstance(chunks, list)
        assert all(isinstance(c, Document) for c in chunks)

    def test_chunks_have_required_metadata_keys(self):
        docs = [Document(page_content=SINGLE_RECIPE, metadata={"source": "test.md"})]
        chunks = chunk_documents(docs)
        required_keys = {"source", "title", "cuisine", "diet_tags", "time_minutes"}
        for chunk in chunks:
            assert required_keys.issubset(chunk.metadata.keys()), \
                f"Missing keys in chunk metadata: {required_keys - chunk.metadata.keys()}"

    def test_source_metadata_propagated(self):
        docs = [Document(page_content=SINGLE_RECIPE, metadata={"source": "myfile.md"})]
        chunks = chunk_documents(docs)
        for chunk in chunks:
            assert chunk.metadata["source"] == "myfile.md"

    def test_multiple_documents_all_chunked(self):
        docs = [
            Document(page_content=SINGLE_RECIPE, metadata={"source": "a.md"}),
            Document(page_content="# Pasta\nQuick pasta recipe. 20 minutes.", metadata={"source": "b.md"}),
        ]
        chunks = chunk_documents(docs)
        sources = {c.metadata["source"] for c in chunks}
        assert "a.md" in sources
        assert "b.md" in sources

    def test_large_document_is_split_into_multiple_chunks(self):
        docs = [Document(page_content=LARGE_RECIPE, metadata={"source": "large.md"})]
        chunks = chunk_documents(docs)
        assert len(chunks) > 1

    def test_empty_document_list_returns_empty(self):
        chunks = chunk_documents([])
        assert chunks == []

    def test_chunk_content_is_non_empty(self):
        docs = [Document(page_content=SINGLE_RECIPE, metadata={"source": "test.md"})]
        chunks = chunk_documents(docs)
        for chunk in chunks:
            assert len(chunk.page_content.strip()) > 0

    def test_cuisine_metadata_correctly_detected(self):
        recipe = "# Italian Pasta\nCuisine: Italian\nPasta with tomato sauce."
        docs = [Document(page_content=recipe, metadata={"source": "italian.md"})]
        chunks = chunk_documents(docs)
        assert any(c.metadata["cuisine"] == "Italian" for c in chunks)

    def test_diet_tags_metadata_detected(self):
        recipe = "# Vegan Salad\nThis is a vegan gluten-free salad recipe."
        docs = [Document(page_content=recipe, metadata={"source": "salad.md"})]
        chunks = chunk_documents(docs)
        diet_tags_all = [tag for c in chunks for tag in c.metadata.get("diet_tags", [])]
        assert "vegan" in diet_tags_all
