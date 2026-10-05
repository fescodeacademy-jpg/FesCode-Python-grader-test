"""The checks your work must pass. Run them yourself with: pytest -v"""
from src.solution import top_n, word_count


def test_counts_words_ignoring_case_and_punctuation():
    assert word_count("Hi hi, there!") == {"hi": 2, "there": 1}


def test_empty_text_has_no_words():
    assert word_count("") == {}


def test_top_n_orders_by_count_then_alphabet():
    counts = {"b": 2, "a": 2, "c": 5, "d": 1}
    assert top_n(counts, 3) == ["c", "a", "b"]


def test_top_n_with_more_than_there_are():
    assert top_n({"a": 1}, 5) == ["a"]
