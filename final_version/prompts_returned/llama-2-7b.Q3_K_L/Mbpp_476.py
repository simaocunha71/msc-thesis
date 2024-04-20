"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
class Solution:
    def getSum(self, nums):
        return max(nums) if len(nums) > 0 else -1;
