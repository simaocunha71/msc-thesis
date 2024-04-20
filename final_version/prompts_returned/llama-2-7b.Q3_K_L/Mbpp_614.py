"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
class Solution:
    def cumulativeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. Create a stack and push in the values
        2. Remove all values that are not there in the list
        3. Calculate the cummulative sum of the elements that are present in the list
            if any
        """
        if len(nums) == 0: return 0
        stack = []
        for i, item in enumerate(nums):
            if nums[i] not in stack:
                stack.append(item)
        
        if not stack: return 0
        for x in stack:
            res += 1
        else: return res