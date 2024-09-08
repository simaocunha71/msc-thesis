"""
This problem can be solved by using dynamic programming.

We can start from the top-left cell and move right or down to the bottom-right cell. For each cell, we can calculate the maximum average of the path that ends at that cell. The maximum average of the path that ends at the cell (i, j) can be computed as max(maxAverageOfPath(i-1, j), maxAverageOfPath(i, j-1)) + cost[i][j] / 2.

The base case is the top-left cell, where the maximum average of the path that ends at the cell (0, 0) is the cost of the cell divided by 2.

Finally, we return the maximum average of the path that ends at the bottom-right cell.
"""

def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = matrix[0][0] / 2.0
    
    # Initialize first row
    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], matrix[0][j] / 2.0) + matrix[0][j] / 2.0

    # Initialize first column
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], matrix[i][0] / 2.0) + matrix[i][0] / 2.0

    # Fill in the rest of the dp table
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], matrix[i][j] / 2.0) + matrix[i][j] / 2.0

    return dp[-1][-1]

assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
This solution has a time complexity of O