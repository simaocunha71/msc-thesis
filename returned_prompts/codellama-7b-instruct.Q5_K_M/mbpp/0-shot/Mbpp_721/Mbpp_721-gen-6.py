def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [ [0] * N for _ in range(N) ]
    for i in range(N):
        dp[i][i] = matrix[i][i]
    for i in range(N-1):
        dp[i][i+1] = max(matrix[i][i], matrix[i+1][i])
    for i in range(2, N):
        for j in range(i+1, N):
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][N-1] / (N*N)
"""