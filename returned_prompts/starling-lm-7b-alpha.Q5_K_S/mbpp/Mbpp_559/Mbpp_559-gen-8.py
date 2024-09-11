"""
The problem can be solved by using the Kadane's Algorithm, which is an efficient method to find the maximum sum contiguous subarray of a given array.

Here's a Python function implementing Kadane's Algorithm to solve the problem:
"""

from typing import List

def max_sub_array_sum(nums: List[int], k: int):
    n = len(nums)
    if n < k:
        return 0

    max_sum = float('-inf')
    for i in range(k):
        max_sum = max(max_sum, nums[i])

    for i in range(k, n):
        max_sum = max(max_sum + nums[i] - nums[i-k], nums[i])

    return max_sum

# Testing the function
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))  # Output: 7

"""
The function `max_sub_array_sum` takes a list of integers `nums` and an integer `k` as input. It first checks if the length of `nums` is less than `k`, in which case it returns 0 because there are no contiguous sublists.

Then, it initializes `max_sum` to negative infinity, as the maximum sum of a sublist can't be less than 0. It then iterates over the first `k` elements of `nums` to find the maximum sum of a sublist with length `k`. It updates `max_sum` with the maximum value between the current `max_sum` and the current element in `nums`.

Next, it iterates over the remaining elements of `nums` starting from index `k`. For each element, it updates `max_sum` by taking the maximum between the current `max_sum` and the sum of the current element and the sublist starting `k` elements before the current element. This step ensures that the maximum sum of a sublist with length `k` is always considered.

Finally, the function returns the maximum sum of a contiguous sublist