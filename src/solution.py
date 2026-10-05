"""Your work goes here. Replace each function body with your own code."""
import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """How many times each word appears, ignoring case and punctuation.

    word_count("Hi hi, there!") == {"hi": 2, "there": 1}
    """
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", text.lower())
    return dict(Counter(words))


def top_n(counts: dict[str, int], n: int) -> list[str]:
    """The n most frequent words, most frequent first; ties in alphabetical order."""
    return sorted(counts, key=lambda w: (-counts[w], w))[:n]
