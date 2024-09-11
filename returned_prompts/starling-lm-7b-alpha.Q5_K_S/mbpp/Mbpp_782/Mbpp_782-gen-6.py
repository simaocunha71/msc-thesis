"""
from itertools import combinations
from itertools import chain

def odd_length_sum(nums):
    odd_length_subarrays = list(chain(*map(lambda x: combinations(nums, x), range(1, len(nums) + 1))))
    return sum(sum(subarray) for subarray in odd_length_subarrays if len(subarray) % 2 != 0)
"""

def odd_length_sum(nums):
    """
    Find the sum of all odd length subarrays of nums.
    """
    total_sum = 0
    for start_index in range(len(nums)):
        for end_index in range(start_index + 1, len(nums) + 1):
            total_sum += sum(nums[start_index:end_index])
            if (end_index - start_index) % 2 != 0:
                total_sum -= sum(nums[start_index:end_index])
    return total_sum

assert odd_length_sum([1,2,4]) == 14


def odd_length_sum(nums):
    """
    Find the sum of all odd length subarrays of nums.
    """
    total_sum = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            total_sum += sum(nums[i:j])
            if (j - i) % 2 != 0:
                total_sum -= sum(nums[i:j])
    return total_sum

assert odd_length_sum([1,2,4]) == 14


def odd_length_sum(nums):
    """
    Find the sum of all odd length subarrays of nums.
    """
    total_sum = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            total_sum += sum(nums[i:j])
            if (j - i) % 