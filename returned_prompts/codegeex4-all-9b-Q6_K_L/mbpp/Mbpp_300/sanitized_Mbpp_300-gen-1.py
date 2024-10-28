def count_binary_seq(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return sum(dp[n])