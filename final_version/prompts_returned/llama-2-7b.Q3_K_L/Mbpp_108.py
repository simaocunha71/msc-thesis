"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""
from typing import List

def merge_sorted_list(a: List[int], b: List[int]) -> List[int]:
    c = []
    x = a.pop(-1)
    while x in [x for x in b]:
        if a[-1] == x:
            del a[-1]
        else:
            c += list(a)
            
    return c + list(b)
