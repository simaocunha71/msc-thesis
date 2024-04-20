"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""
import math
from typing import Optional, List

def closest_number(val: int, nums: List[int]):
    if val in set(map(math.ceil, map(math.floor, nums))):
        return math.ceil(val)
    else:
        closest = 10**9 + val - len(nums) // 2
        for i in range(len(nums)):
            if val <= nums[i] < closest:
                closest = nums[i]
        return closest