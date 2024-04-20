"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
class Solution:
    def findFirstDuplicate(self, nums):
        """
        :param nums: An array containing all duplicate numbers.
        :return: The index of first occurrence of the given duplicate number.
        """ (2,5)
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == nums[-1]:
                return i
