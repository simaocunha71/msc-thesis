def count_binary_seq(n):
    dp = [[0]*(2*n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(2*n+1):
            dp[i][j] = dp[i-1][j-1] if j-1 >= 0 else 0
            dp[i][j] += dp[i-1][j+1] if j+1 <= 2*n else 0
    return sum(dp[n][n:2*n+1])