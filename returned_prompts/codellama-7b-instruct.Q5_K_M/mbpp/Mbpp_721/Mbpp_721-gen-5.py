"""
dp[i][j][k] = max(dp[i-1][j-1][k-1], dp[i-1][j][k], dp[i][j-1][k])

dp[i][j][k] = dp[i-1][j-1][k-1] if the path is (i-1, j-1)
dp[i][j][k] = dp[i-1][j][k] if the path is (i-1, j)
dp[i][j][k] = dp[i][j-1][k] if the path is (i, j-1)

"""
