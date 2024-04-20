"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
class Solution:
    def find_max(self, nums):
        """return the index of the max element in given list."""
        index = -1
        maxi = 0
        for i in range(len(nums)):
            if len(nums[i]) > maxi:
                maxi = len(nums[i])
                index = i
        return index, maxi
        