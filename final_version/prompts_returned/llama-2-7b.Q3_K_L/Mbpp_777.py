"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
class Solution:
    def findSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, res = 0, 0
        for val in nums:
            if not (cnt & 1):
                res += val
            else:
                cnt ^= 1
            
        return res
