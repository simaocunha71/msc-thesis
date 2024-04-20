"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""
from typing import List

def max_sub_array(nums:List[int]) -> int :
    """
    Time complexity of O(n) by using 2 nested for loop.
    Space complexity is O(1).
    """
    max_sub_array_sum = 0

    def find_max():
        """
        Find the maximum sum in a sub-list of an array of given length.
        :param nums: Array to which sub list will be added.
        :return: Maximum sum in the sub-list that was found and the index of it.
        """
        max_sum = 0
        for i, val in enumerate(nums):
            if i == len(nums) - 1:
                break
            while nums[i+1] > val:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        if max_sum < (val + nums[i+1]):  # Check whether we can find a larger sum. If so, exit now.
            return val, i + 1
        
        sub_array = nums[max(0, i-MAX_SUB_ARRAY_SIZE) : max(0, i+MAX_SUB_ARRAY_SIZE)]   # Creating the sub list to check for the maximum sum. Note that the upper limit should be one less than the length of the array so that we do not run into an out of bounds error.
        return max(sub_array), len(sub_array)

    for i in range(len(nums)):
        j = find_max()[1] - 1
        
        if i == len(nums)-1:
            max_sub_array_sum += (j+1)*(nums[i])
        else:
            max_sub_array_sum += max_sub_array_sum + j*(nums[i])
            
    return max_sub_array_sum