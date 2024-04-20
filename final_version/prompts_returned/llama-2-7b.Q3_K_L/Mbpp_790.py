"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""
class Solution:
    def evenPosition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size % 2 != 0 or size == 0: # special cases
            return False

        odd_indexes = [i for i in range(size - 1, -1, -1)]
        if sum(nums[odd_index] * nums[odd_index] for odd_index in odd_indexes) % 2 == 0: # check if the total is even, return true or false
            return True
        else:
            return False