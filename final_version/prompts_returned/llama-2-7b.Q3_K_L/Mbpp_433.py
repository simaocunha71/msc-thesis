"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
class Solution:
    def checkGreater(self, nums: List[int], target: int) -> bool:
        for value in nums:
            if value > target:
                return True