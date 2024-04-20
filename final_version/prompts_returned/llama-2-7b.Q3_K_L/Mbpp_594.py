"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
class Solution:
    def diffEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)  # length of the list
        ret = 0  # return
        i = 1 if length % 2 == 1 else -1  # start from even index
        while i <= length // 2 - 1:
            left = nums[i]  # Get first odd number
            right = nums[i + 1]  # Get first even number
            ret += (left + right) % 10 - (right + left) % 10
            i += 1
        return ret
