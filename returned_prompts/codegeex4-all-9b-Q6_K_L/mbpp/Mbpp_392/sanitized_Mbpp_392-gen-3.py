def get_max_sum(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    dp[5] = 5
    for i in range(6, n + 1):
        dp[i] = max(dp[i // 2] + dp[i // 3] + dp[i // 4] + dp[i // 5], i)
    return dp[n]