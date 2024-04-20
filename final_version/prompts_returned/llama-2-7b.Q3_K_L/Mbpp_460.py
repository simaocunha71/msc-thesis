"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
from typing import List

def extract(lst: List[List]) -> List:
    """Return the first element of each sublist."""
    return lst[-1]