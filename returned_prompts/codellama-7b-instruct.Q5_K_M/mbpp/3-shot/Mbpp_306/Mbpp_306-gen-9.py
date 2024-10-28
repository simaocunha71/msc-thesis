
def max_sum_increasing_subseq(arr, n, k, i):
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        dp[j] = max(dp[j - 1], dp[j - 1] + arr[j - 1])
        if j >= k and j > i:
            dp[j] = max(dp[j], dp[j - 1] + arr[j])
    return dp[n]


