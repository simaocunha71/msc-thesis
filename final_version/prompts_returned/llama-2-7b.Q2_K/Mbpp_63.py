"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
class Solution:
    def maxDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
# Write your code here
        if not nums or len(nums) == 0 or len(nums) <= 1:
            return -1
        
        max_difference = min(nums[0], nums[1])
        for idx, i in enumerate(range(2,len(nums))):
            if (max_difference + nums[i] < nums[i+idx+1]):
                max_difference += nums[i+idx+1]-max_difference - 1
        return max_difference