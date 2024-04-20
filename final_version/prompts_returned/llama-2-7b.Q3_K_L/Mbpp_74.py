"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
from typing import List, Optional

def is_samepatterns(p: str, patterns: List[str]) -> bool:
    """
    :type p: str
    :rtype: bool
    :return: True if the pattern is a sequence of same colors in order.
    """
    if not patterns:
        return False  # Empty list of pattern, so it's not the same color
    else:
        return any(len(p) == len(p_i) for p_i in patterns) and all(
            char in p for i, char in enumerate(patterns))
