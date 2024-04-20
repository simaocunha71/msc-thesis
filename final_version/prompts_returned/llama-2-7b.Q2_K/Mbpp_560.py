"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""
from typing import *
def union_elements(a: Tuple[int], b: tuple):
    """Write a function to find the union of the elements of two given tuples and output them in sorted order.
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)"""
    # a = [3, 4, 5]
    # b = [5, 7, 4]
    sorted_a = sorted(sorted(set(a)) + set(b))
    return sorted_a