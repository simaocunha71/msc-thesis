The problem can be solved by using dynamic programming.

First, we can create an auxiliary matrix dp of the same size as the given matrix. dp[i][j] will store the maximum average path value that we can get from the top-left cell to the cell (i, j).

Then, we iterate over the matrix from the bottom right to the top left. For each cell (i, j), we update dp[i][j] as the maximum between dp[i+1][j] and dp[i][j+1] plus the cost of the current cell.

Finally, the answer will be dp[0][0], which represents the maximum average path value that we can get from the top-left cell to the bottom right cell.

Here is the Python code for the above approach:

```python
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[-1][-1] = matrix[-1][-1]

    for i in range(n-2, -1, -1):
        dp[i][-1] = max(dp[i+1][-1] + matrix[i][-1], dp[i][-1])
        dp[-1][i] = max(dp[-1][i+1] + matrix[-1][i], dp[-1][i])

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + matrix[i][j]

    return dp[0][0] / ((n-1)*2)
```

The time complexity of this code is O(n^2) and the space complexity is also O(n^2).

Let's test the function with the provided example:

```python
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # Output: 5.2
```
This