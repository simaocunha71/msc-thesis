def get_max_sum(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(i, dp[i // 2] + dp[i // 3] + dp[i // 4] + dp[i // 5])
    return dp[-1]