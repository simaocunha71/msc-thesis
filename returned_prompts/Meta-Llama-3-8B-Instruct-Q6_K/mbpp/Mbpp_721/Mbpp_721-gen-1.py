```
def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0.0] * n for _ in range(n)]
    dp[0][0] = cost[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    max_avg = 0.0
    for i in range(1, n):
        for j in range(1, n):
            avg = dp[i][j] / (i + j)
            max_avg = max(max_avg, avg)
    return max_avg
```


The idea is to use dynamic programming to calculate the total cost of each path. Then, we calculate the average cost of each path and find the maximum average. We initialize a 2D array `dp` of size `n x n` where `dp[i][j]` represents the total cost of the path from the top-left cell to the cell at `(i, j)`. We fill this array in a bottom-up manner. Then, we iterate over all cells in the array and calculate the average cost of each path. We keep track of the maximum average cost and return it at the end. The time complexity is O(n^2) and the space complexity is also O(n^2). 

Note: The problem statement doesn't specify what to do if there are multiple paths with the same maximum average. In this solution, we simply return the maximum average. If we need to return all paths with the maximum average, we would need to modify the solution to keep track of all such paths. 

Also, note that the problem statement doesn't specify what to do if the input is not a square matrix. In this solution, we assume that the input is always a square matrix. If the input can be a non-square matrix, we would need to add additional checks and handling. 

The unit test `assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3,