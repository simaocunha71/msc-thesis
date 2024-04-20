"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
class Solution:
    def nth_nums(self, nums, n):
        """
         :param nums: a list of integers
         :param n: an integer
         :return: returns the result of n-th power of each number in nums
        """
        if not isinstance(nums,list) or len(nums)<1:
            return [None]
        l = []
        for i in range(len(nums)):
            tmp_list=[pow(i,j,n) for j in range(1,n+1)]
            l.extend(tmp_list)
        return l