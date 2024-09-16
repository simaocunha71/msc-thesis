"""
def maxAverageOfPath(matrix):
    # write your code here
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    max_avg = 0
    for i in range(n):
        dp[i][i] = matrix[i][i]
        max_avg = max(max_avg, dp[i][i])
    for i in range(n - 1):
        for j in range(i + 1, n):
            dp[i][j] = max(matrix[i][j], dp[i][j - 1], dp[i + 1][j])
            max_avg = max(max_avg, dp[i][j])
    for i in range(n):
        for j in range(n):
            if i != j:
                dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i + 1][j], dp[i + 1][j - 1])
                max_avg = max(max_avg, dp[i][j])
    return max_avg / (n * n)
"""