"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
from typing import List

def find_first_occurrence(nums:List[int], number:int)->int:
    """Time complexity: O(n)"""
    idx = -1
    
    for i in range(len(nums)):
        if nums[i] == number:
            return i
        
    # if we can't find the element, index should be set to length of array
    return len(nums)