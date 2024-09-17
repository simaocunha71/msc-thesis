def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    max_avg = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
            avg = dp[i][j] / (i + 1)
            max_avg = max(max_avg, avg)
    return max_avg