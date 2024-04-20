"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
from typing import List

def sum_range_list(nums:List[int], idxStart, idxEnd):
    if idxStart == idxEnd:
        return nums[-idxStart]
    else:
        sum = 0
        for i in range(idxStart, idxEnd+1):
            sum += nums[i]
        return sum