def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][0] = matrix[i][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[N-1][N-1]/2