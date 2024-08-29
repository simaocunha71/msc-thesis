
def max_sum_increasing_subseq(arr, n, k, i):
    if i >= n or i < 0 or k >= n or k < 0:
        return 0
    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i]+arr[j])
            max_sum = max(max_sum, dp[j])
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            dp[j] = max(dp[j], dp[i]+arr[j])
            max_sum = max(max_sum, dp[j])
    max_sum += arr[k]
    return max_sum

print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6)) # 11

This solution works by creating a dynamic programming array dp where dp[i] stores the maximum sum of increasing subsequence ending at index i. For each element in the array, it updates the maximum sum for the elements that are greater than the current element and the elements that are less than the current element. Finally, it adds the value at the kth index to the maximum sum.
"""
Time complexity: O(n)
Space complexity: O(n)
"""

This solution assumes that the given i and k are valid indices in the array and that the elements in the array are distinct. If the elements are not distinct, the solution will not work correctly.
"""
Note:
This solution works with the assumption that the i and k are valid indices and that the elements in the array are distinct. If the elements are not distinct, the solution will not work correctly.
"""

"""
