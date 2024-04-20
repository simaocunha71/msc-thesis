"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
from typing import List

def count_same_pair(a:List[int], b:List[int]) -> int:
    """
    Count indices of the same value in list a and list b.
    The length of both lists must be the same (i.e., len(a) == len(b)).
    Args:
        a, b: Lists representing inputs
    Returns: 
        count_same_pair(a, b): count of indices of the same values in list a and list b.
    """

    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            c+=1
        
    return c