def next_Perfect_Square(n):
    x = int(n**0.5)
    while True:
        y = x*x
        if y > n:
            return y
        x += 1

# Driver code
print(next_Perfect_Square(35))













"""
Given an integer array arr, and two integers d and k, your task is to find the maximum value of subarray sum of length k. In other words, you need to find the maximum value of arr[i:i+k]. In this problem, all elements of the array are positive integers.

For example, if arr = [1, 3, 2, 1, 4, 3, 2], d = 3 and k = 3, then the maximum sum of subarray of length k is 10, which is the sum of [2, 1, 4].

Here is the function signature for the problem:

def max_sum_subarrays(arr, d, k):
# Inputs:
#   arr: A list of positive integers. The length of arr is at least d.
#   d: An integer, the length of subarray.
#   k: An integer, the length of subarray.

# Returns:
#   An integer, the maximum value of sum of subarray of length k.

"""

def max_sum_subarrays(arr, d, k):
    if d >= len(arr):
        return max(arr[:k])
    else:
        window_start = 0
        window_sum = sum(arr[i] for i in range(d))
        max_sum = window_sum
        for i in range(d, len(arr)):
            window_sum = window_sum - arr[i-d] + arr[i]
            max_sum = max(max_sum, window_sum)
        return max_sum

arr = [1, 3, 2, 1, 4, 3, 2]
d = 3
k = 3
print(max_sum_subarrays(arr, d, k))
