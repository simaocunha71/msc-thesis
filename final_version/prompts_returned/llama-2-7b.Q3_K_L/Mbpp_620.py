"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
from typing import List

def max_divisors(nums:List[int]):
    """
    :type nums: [int],
    """
    return sum([i * j for i in range(len(nums)) for j in range(i+1, len(nums)+1) if nums[i]%nums[j] == 0])