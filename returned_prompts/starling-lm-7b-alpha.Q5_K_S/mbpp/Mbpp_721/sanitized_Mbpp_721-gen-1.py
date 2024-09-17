def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = matrix[0][0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + matrix[i][0] / 2
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j] / 2
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j] / 2
    return dp[N-1][N-1]