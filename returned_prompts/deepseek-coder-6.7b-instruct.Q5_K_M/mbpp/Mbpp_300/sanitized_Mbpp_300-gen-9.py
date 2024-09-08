def count_binary_seq(n):
    dp = [[0]*(2*n+1) for _ in range(2*n+1)]
    dp[0][0] = 1
    dp[1][0] = 1
    for i in range(2, 2*n+1):
        dp[i][0] = 0
        dp[0][i] = 0
    for i in range(1, 2*n+1):
        for j in range(1, 2*n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]