"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
class Solution:
    def secondSmallest(self, nums):
        # write your code here
        return max(max(nums), min(nums))