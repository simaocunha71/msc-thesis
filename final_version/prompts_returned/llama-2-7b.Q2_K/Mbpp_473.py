"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
from typing import Any, List

def tuple_intersection(tuples:List[Any]) -> list:
    """Returns the elements of a given tuple having common tuples in the intersection tuples."""
    if not tuples or len(tuples) == 0: return []
    intersection = set()
    for i, tupe in enumerate(tuples):
        curr_intersection = intersection.copy()
        curr_intersection |= intersection.intersection(*tupe)
        intersection |= curr_intersection - curr_intersection
    return list(intersection)
