"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
from typing import Any, List

def is_samepatterns(
    word: str, 
    patterns:List[str]
) -> bool:
    """Check the pattern and return True if they are equal."""
    if len(word) != len(patterns):
        raise ValueError("Word length is different than expected.")    
    for i in range(len(word)):
        if word[i] == patterns[i]:
            continue
        else:
            return False
    print('Returning True')
    return True