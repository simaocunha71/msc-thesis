def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[-1][-1] = matrix[-1][-1]

    for i in range(n-2, -1, -1):
        dp[i][-1] = max(dp[i+1][-1] + matrix[i][-1], dp[i][-1])
        dp[-1][i] = max(dp[-1][i+1] + matrix[-1][i], dp[-1][i])

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + matrix[i][j]

    return dp[0][0] / ((n-1)*2)