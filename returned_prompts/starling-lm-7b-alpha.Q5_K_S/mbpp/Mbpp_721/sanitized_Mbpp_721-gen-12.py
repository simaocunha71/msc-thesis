def maxAverageOfPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(m):
        for j in range(n):
            if i>0:
                dp[i][j] += dp[i-1][j]+matrix[i][j]
            if j>0:
                dp[i][j] += dp[i][j-1]+matrix[i][j]
    return max(dp[m-1][n-1] / (n+m-1),dp[m-1][n-2] / (n+m-2))