def maxAverageOfPath(matrix):
    dp = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        dp[i][0] = matrix[i][0]
    for j in range(len(matrix)):
        dp[0][j] = matrix[0][j]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[len(matrix)-1][len(matrix)-1] / (len(matrix) + len(matrix)-1)