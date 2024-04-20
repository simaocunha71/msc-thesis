"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
from typing import Tuple

def tuple_intersection(tuples:Tuple[Tuple]): return {t for t in tuples if t}
# Time complexity: O(M * log(N)) - M is the number of elements and N is the number of unique elements
# Space complexity: O(1) - 1 additional variable space to store the list to check intersection
