def maxAverageOfPath(mat):
    m = len(mat)
    n = len(mat[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = mat[i][0]
    for j in range(n):
        dp[0][j] = mat[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + mat[i][j]
    return dp[m - 1][n - 1] / (m + n - 1)