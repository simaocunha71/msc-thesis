def maxAverageOfPath(mat: list) -> float:
    n = len(mat)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][0] = mat[i][0]
    for j in range(1, n):
        dp[0][j] = mat[0][j] + dp[0][j-1]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = mat[i][j] + max(dp[i-1][j], dp[i][j-1])
    return dp[n-1][n-1]/n