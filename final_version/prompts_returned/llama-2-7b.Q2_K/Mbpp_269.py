"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""
from typing import Optional

def ascii_value(ch: str) -> int or None:
    if ch in 'a-z':
        return ord('a') - ord('z') + 1
    elif ch in '0-9':
        return ord('0') - ord('9') + 1
    else:
        return None