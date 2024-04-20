"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
from typing import Optional

def pancake_sort(nums: list) -> None: # pylint: disable=unused-argument
    """Pancakes sort the items in the array."""
    
    def helper(nums, i, j):
        if nums[i] < nums[j]:
            swap = nums[i]
            nums[i], nums[j] = nums[j], nums[i]  # pylint: disable=assignment-within-loop
            helper(nums, i+1, j)
            helper(nums, i+1, j-1)
            helper(nums, i-1, j)
            helper(nums, i-1, j-1)
            helper(nums, i, j-1)  # pylint: disable=assignment-within-loop
        return swap
    
    nums = sorted(nums, key=helper)
