"""
import math

def maxAverageOfPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j] = matrix[i][j]
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    path = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                path[i][j] = 1
            elif i > 0 and j == 0:
                path[i][j] = path[i - 1][j]
            elif i == 0 and j > 0:
                path[i][j] = path[i][j - 1]
            else:
                path[i][j] = min(path[i - 1][j], path[i][j - 1])
    return dp[-1][-1] / path[-1][-1]
"""
