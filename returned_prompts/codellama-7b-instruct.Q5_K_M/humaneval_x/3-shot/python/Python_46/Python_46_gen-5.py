    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 2
    dp[3] = 0
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
    return dp[n]


