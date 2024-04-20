"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
from typing import List

def pair_wise(lst: List[int]) -> List[List]:
    """
    :type lst: [int]
    :rtype: [[]]
    """
    if len(lst) < 2:
        return []
    result = [(i, i+1) for i in range(len(lst)-1)] + [(i+1, i) for i in range(1,len(lst))]
    print(result)
    return result
