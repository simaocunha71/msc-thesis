
def maxAverageOfPath(matrix):
    size = len(matrix)
    dp = [[0]*size for _ in range(size)]
    dp[0][0] = matrix[0][0]
    for i in range(1, size):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    for i in range(1, size):
        for j in range(1, size):
            dp[i][j] = max(dp[i-1][j]+matrix[i][j], dp[i][j-1]+matrix[i][j])
    return dp[-1][-1]/size


