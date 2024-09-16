"""
def maxAverageOfPath(matrix):
    # Write your code here
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = matrix[i][i]
    for i in range(n - 1):
        dp[i][i + 1] = max(matrix[i][i], matrix[i + 1][i])
    for i in range(n - 2):
        dp[i + 1][i + 1] = max(matrix[i + 1][i + 1], dp[i][i] + matrix[i + 1][i + 1])
    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], dp[i][j - 2] + matrix[i][j])
    return dp[0][n - 1] / (n * n)
"""
