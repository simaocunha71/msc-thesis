
def max_sub_array_sum_repeated(arr, k, n):
    def kadane(arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    arr = arr * k
    return kadane(arr)


print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))  # 30

"""
Explanation:

We first define a function kadane() which finds the maximum subarray sum using Kadane's algorithm. We then repeat the array arr[] k times. The maximum subarray sum of the modified array is then found using kadane() on the repeated array.
"""

"""
Note:

In the above solution, we are taking O(n*k) time complexity which is quite high for larger inputs. There is a more efficient solution using dynamic programming which will take O(n) time complexity.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Q2.** Given an array of integers, find the length of the longest increasing subsequence. The subsequence is formed by deleting some number of elements (possibly none) from the original sequence, leaving the remaining elements in their original order.Example:```Input: [10, 9, 2, 5, 3, 7, 101, 18]Output: 4 Explanation: The longest increasing subsequence is [2, 5, 7, 101]```
<jupyter_code>
def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp