"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
from typing import Callable, List, Optional, Tuple


class Solution(object):
    def __init__(self, func: Callable[[int, int], int]) -> None:
        self._func = func

    def add_pairwise(self, A: List[int]) -> List[int]:
        return [
            self._func(a, b) for a, b in zip(*itertools.combinations(A, 2))]


def find_addition(A: Tuple[int, int], func: Callable[[int, int], int]) -> int:
    """Add the pairwise values of A."""
    return Solution(func).add_pairwise([a, b] for a, b in zip(*A))
