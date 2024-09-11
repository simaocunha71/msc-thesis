Here's one possible way to solve this problem:

```python
def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][0] = matrix[i][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[N-1][N-1]/2
```

In this solution, we initialize a 2D array `dp` to keep track of the maximum sum path from the top-left to each cell in the matrix. We start by filling the first row and column of `dp` with the corresponding values from the input matrix. Then, for each cell starting from the second row and column, we update the value of `dp` by taking the maximum value from the cell above it or the cell on its left, and adding the value of the current cell. Finally, we return the value at the bottom-right cell of `dp`, which represents the maximum sum path from the top-left to the bottom-right cell, and divide it by 2 to get the average.

The time complexity of this solution is O(N^2), where N is the size of the matrix, as we need to iterate through all the cells in the matrix once. The space complexity is also O(N^2), as we need to store the `dp` array with the same size as the input matrix.

This solution works by keeping track of the maximum sum path from the top-left to each cell in the matrix, and then dividing the sum at the bottom-right cell by 2 to get the average. It provides a concise and efficient way to solve the problem.
```

```

```

```

```python

```

```

```

```

```

```

```

```

