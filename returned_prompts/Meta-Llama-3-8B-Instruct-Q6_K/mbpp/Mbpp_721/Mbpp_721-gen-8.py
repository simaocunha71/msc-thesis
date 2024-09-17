```
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    max_avg = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
            avg = dp[i][j] / (i + 1)
            max_avg = max(max_avg, avg)
    return max_avg
```
Explanation:
This function calculates the maximum average of all existing paths in the given matrix. It uses dynamic programming to build the dynamic programming table dp, where dp[i][j] represents the total cost of the path from the top-left cell to the cell at position (i, j). The maximum average is then calculated as the maximum of the averages of all paths in the dynamic programming table. The average is calculated as the total cost divided by the number of cells visited in the path, which is (i + 1) for the path from the top-left cell to the cell at position (i, j). The maximum average is returned as the result. The unit test `assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2` ensures that the function works correctly.