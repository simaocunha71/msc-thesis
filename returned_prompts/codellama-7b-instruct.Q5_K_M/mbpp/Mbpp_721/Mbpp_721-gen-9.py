"""
def maxAverageOfPath(matrix):
    # Write your code here
    n = len(matrix)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            dp[i][j] += matrix[i][j]
    return dp[n - 1][n - 1] / (n * n)
"""
