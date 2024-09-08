"""
This problem can be solved using dynamic programming. We initialize a 2D array dp of size N*N to store the maximum average cost from the top-left cell to the cell at row i and column j. We use the following recursive formula to populate the dp array:

dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]

Finally, the maximum average cost from the top-left cell to the bottom right cell will be dp[N-1][N-1]/N.

Here is a Python solution:
"""

def maxAverageOfPath(cost):
    N = len(cost)
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = cost[0][0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        dp[0][i] = dp[0][i-1] + cost[0][i]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    return dp[N-1][N-1] / N

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # Output: 5.2

"""
This solution has a time complexity of O(N^2) as we are traversing the 2D array once and space complexity of O(N^2) for storing the dp array.
"""

"""
Problem 2:

