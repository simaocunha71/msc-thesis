"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
from typing import Callable, Optional, Union

def text_match_a(first: str) -> bool:
    return bool(first[0].islower()) and first in ["a", "ab"]


def text_match_b(first: str) -> bool:
    """
    match b after a
    1. assert not first[0] == 'a'
    2. assert text_match_three(f"{first}b")
    """
    return (not text_match_a(first)) and text_match_three(f"{first}b")

if __name__ == "__main__":
    pass
