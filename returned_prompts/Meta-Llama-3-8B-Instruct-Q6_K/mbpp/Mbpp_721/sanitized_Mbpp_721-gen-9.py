from typing import List
def maxAverageOfPath(matrix: List[List[int]]) -> float:
    n = len(matrix)
    dp = [[0.0] * n for _ in range(n)]

    for i in range(n):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i][j-1]) / (i + j)

    return max(max(row) for row in dp)