def maxAverageOfPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + matrix[i][j]
    return dp[m - 1][n - 1] / (m + n - 1)