def count_binary_seq(n):
    dp = [[0]*2*n for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, 2*n):
        dp[0][i] = 2*dp[0][i-1]
    for i in range(1, n+1):
        for j in range(2*n):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    return dp[n][2*n-1]