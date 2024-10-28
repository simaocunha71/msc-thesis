
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(dp[i-1][j]+matrix[i][j], dp[i][j-1]+matrix[i][j])
    return dp[-1][-1]/((n-1)*(n-1))

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
"""
This function uses dynamic programming to solve the problem. dp[i][j] is the max cost to reach the cell (i, j) from the top left cell (0, 0), and it is computed by choosing the max cost path from the left cell or the top cell. The final result is dp[-1][-1] divided by (n-1)*(n-1) to compute the average cost. The time complexity is O(n^2) and the space complexity is also O(n^2).
"""

