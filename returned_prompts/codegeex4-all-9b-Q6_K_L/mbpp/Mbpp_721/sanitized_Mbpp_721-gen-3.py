def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    total_cost = dp[n-1][n-1]
    path_count = n * n
    average = total_cost / path_count
    return average