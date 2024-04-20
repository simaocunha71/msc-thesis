"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, cast

T = TypeVar('T', covariant=True)


class Solution:
    def sumNegativenum(self, nums: List[int]) -> int:
        negatve_nums = [n for n in nums if -n < 0]
        return sum(-1 * x for x in negatve_nums)


def test_sum_negativenum():
    solution = Solution()
    assert solution.sumNegativenum([-1, 2, -3, -4, 5]) == -6
