def max_sub_array_sum(nums, k):
    s = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if j - i + 1 == k:
                s += sum(nums[i:j+1])
    return s


def max_sub_array_sum(nums, k):
    return sum(nums[i:i+k] for i in range(len(nums)-k+1))

def max_sub_array_sum(nums, k):
    n = len(nums)
    sums = [0] * (n + 1)
    for i in range(1, n+1):
        sums[i] = sums[i - 1] + nums[i - 1]
    return max(sums[i + k] - sums[i] for i in range(n - k + 1))

def max_sub_array_sum(nums, k):
    return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))

def max_sub_array_sum(nums, k):
    return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))


"""
The maximum sum contiguous subarray problem is a classical optimization problem in combinatorial optimization.

Given an integer array nums, find the contiguous subarray within the array that has the largest sum and return its sum.

Example 1:

Input: [-2,1,-3,4,-1,2,1,-5,4], k = 6
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Note:

1 <= k <= 2 * 10^4
-10^5 <= nums[i] <= 10^5
"""


def max_sub_array_sum(nums, k):
    n = len(nums)
    if n <