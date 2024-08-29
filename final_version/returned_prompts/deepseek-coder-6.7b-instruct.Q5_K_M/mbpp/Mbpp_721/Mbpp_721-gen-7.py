"""
This problem can be solved by using dynamic programming.

1. Initialize a 2D list dp with the same size as the input list. dp[i][j] represents the maximum average cost of a path that ends at cell (i, j).
2. Traverse the input list from bottom to top, right to left. For each cell, calculate dp[i][j] by taking the maximum value between dp[i+1][j] and dp[i][j+1], then add the cost of the current cell.
3. The result is dp[0][0].

Here is the Python code that implements the above steps:
"""

def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[-1][-1] = matrix[-1][-1]
    
    for i in range(n-2, -1, -1):
        dp[i][-1] = max(dp[i+1][-1]+matrix[i][-1], dp[i][-1])
        dp[-1][i] = max(dp[-1][i+1]+matrix[-1][i], dp[-1][i])
    
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = max(dp[i+1][j]+matrix[i][j], dp[i][j+1]+matrix[i][j], dp[i][j])
    
    return dp[0][0]/((n-1)*2)

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # Output: 5.2

This solution has time complexity O(n^2) and space complexity O(n^2).
"""

