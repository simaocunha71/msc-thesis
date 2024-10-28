    dp = [0, 0, 2, 0]

    for i in range(4, n + 1):
        dp[i % 4] = dp[(i - 1) % 4] + dp[(i - 2) % 4] + dp[(i - 3) % 4] + dp[(i - 4) % 4]

    return dp[n % 4]


