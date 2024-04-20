"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
from typing import List, Union

def count_non_empty_str(s: str) -> int:
    """
    @param s: The original string.
    @return: An integer representing the number of non-empty substrings.
    """
    res = 0
    
    for i, j in enumerate(s):
        if i != j + 1 and j != len(s) - 1:
            res += 1
        
    return res