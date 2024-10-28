def max_sum_increasing_subseq(arr, i, k, n):
    dp = [0] * n
    for idx, val in enumerate(arr):
        if idx <= i:
            dp[idx] = val
        else:
            dp[idx] = max(dp[idx - 1], dp[idx])

    for idx, val in enumerate(arr):
        if idx >= k:
            dp[idx] = max(dp[idx - 1], dp[idx] + val)
    return dp[n - 1]