"""
def max_sum(arr):
    # Find the maximum sum of a bitonic subsequence.
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i] + arr[i], dp[i - 1] + arr[i])
    return dp[n]
"""
