"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""
from typing import List

def first_odd(nums:List[int]) -> int:
    start = 0
    end = len(nums) - 2
    odd = []
    for i in range(start + 1, end):
        if nums[i] % 2 == 1:
            odd.append(nums[i])
    return odd[-1] if odd else None