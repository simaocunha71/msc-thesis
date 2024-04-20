"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
class Solution:
    def findMin(self, nums):
        if not len(nums) <= 1 or not isinstance(nums, list) : return []

        count = 0;
        min_len = len(nums[0])
        for i in range(len(nums)):
            cnt = nums[i][:].count(min(nums[i]))
            if (cnt > 0):
                min_len = max(min_len,cint)
                count += 1
        
        return [x for x in nums if len(x) == min_len and cnt >= count]