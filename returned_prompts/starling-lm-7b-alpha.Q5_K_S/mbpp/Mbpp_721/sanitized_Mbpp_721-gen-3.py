def maxAverageOfPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
            elif i != 0 and j != 0:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    return float(dp[m - 1][n - 1]) / (m + n - 1)