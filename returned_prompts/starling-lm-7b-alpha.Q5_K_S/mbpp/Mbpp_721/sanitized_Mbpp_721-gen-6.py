def maxAverageOfPath(mat):
    N = len(mat)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = mat[0][0]
    for i in range(N):
        for j in range(N):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + mat[i][j]
            elif i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + mat[i][j]
            elif i != 0 and j != 0:
                dp[i][j] = mat[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    return float(dp[-1][-1]) / (N * N)