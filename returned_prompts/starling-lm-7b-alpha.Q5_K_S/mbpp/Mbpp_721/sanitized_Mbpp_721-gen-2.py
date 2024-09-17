def maxAverageOfPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    return dp[m - 1][n - 1] / (m + n - 1)
matrix = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]