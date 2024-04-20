"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""
from typing import List

def two_unique_nums(nums: List[int]) -> List[int]:
    """Ask for a list of numbers and find the unique number in them."""
    
    set_num = set()
    num_set = set()
    
    for i in range(len(nums)):
        num_set.add(nums[i]) 
    return [value for value, _ in sorted(list(num_set), key=lambda x: x)]
