def get_max_sum(n):
    if n < 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = max(dp[i // 2] + dp[i // 3] + dp[i // 4] + dp[i // 5], i)

    return dp[n]