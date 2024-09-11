def toggle_middle_bits(n):
    return int('1' + bin(n)[2:][:-1] + '1', 2)

# Test
print(toggle_middle_bits(9))





"""
Given an array of integers, return the length of the longest subarray where all the elements are between 1 and k.
In other words, we're looking for the longest subarray that doesn't contain any number outside the range from 1 to k, inclusive.

Example:

For input [1, 3, 3, 3, 4, 3, 2, 3, 1], the output should be 5. The longest subarray that doesn't contain any number outside the range from 1 to 3 is 3, 3, 3, 4, 3.

For input [6, 5, 4, 3, 2, 1], the output is 6. The longest subarray that doesn't contain any number outside the range from 1 to 5 is 5, 4, 3, 2, 1.

For input [1, 2, 3, 4, 5], the output is 5. The longest subarray that doesn't contain any number outside the range from 1 to 5 is 1, 2, 3, 4, 5.

For input [3, 4, 3, 3, 4, 3, 2, 3, 1], the output is 6. The longest subarray that doesn't contain any number outside the range from 1 to 3 is 3, 3, 4, 3, 3, 4.

For input [1, 1, 1, 1, 1], the output is 5. The longest subarray that doesn't contain any number outside the range from 1 to 1 is 1, 1, 1, 1, 1.
"""

def longest_subarray(nums):
    nums_set = set(nums)
    k = max(nums_set)
    return max([i for i in range(len(nums)) if nums[