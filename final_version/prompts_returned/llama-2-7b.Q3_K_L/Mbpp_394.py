"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
from typing import Optional

def check_distinct(tuple: tuple) -> bool:
    """Create your own function implementation here."""

    if len(tuple) < 2:
        return True

    for i in range(len(tuple)):
        if tuple[i] == tuple[i + 1]:
            return False

    return True