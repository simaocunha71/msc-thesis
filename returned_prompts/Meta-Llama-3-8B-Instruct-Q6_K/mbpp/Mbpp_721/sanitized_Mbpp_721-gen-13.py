def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][0] = matrix[i][0]
    for j in range(N):
        dp[0][j] = matrix[0][j]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i][j-1])
    max_sum = 0
    for i in range(N):
        for j in range(N):
            max_sum = max(max_sum, dp[i][j])
    max_average = max_sum / (N * N)
    return round(max_average, 1)