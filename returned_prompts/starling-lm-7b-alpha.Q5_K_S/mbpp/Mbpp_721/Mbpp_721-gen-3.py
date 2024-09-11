```
def maxAverageOfPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
            elif i != 0 and j != 0:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    return float(dp[m - 1][n - 1]) / (m + n - 1)
```

Explanation
The solution is to use dynamic programming. We start by initializing a 2D array to store the maximum sum of paths to the current cell. We start with the first cell and update the array by adding the current cell's cost to the maximum sum of the previous cell. We use the maximum sum to avoid negative values in the path. Finally, we divide the sum of the bottom right cell by the number of cells visited (m + n - 1) to get the average.

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Test Cases
test1 = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]
assert maxAverageOfPath(test1) == 5.2
```

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 