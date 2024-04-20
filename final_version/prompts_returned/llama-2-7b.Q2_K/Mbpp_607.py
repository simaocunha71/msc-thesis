"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
from typing import Any

def find_literals(s: str, pattern : str) -> (str, int, int):
    """Return substring (s), start index and end index."""
    return s.find(pattern), s.rfind(pattern), len(s)
