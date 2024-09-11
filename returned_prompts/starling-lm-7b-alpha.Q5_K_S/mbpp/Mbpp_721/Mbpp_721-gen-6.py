The above problem can be solved using the concept of Dynamic Programming.

The idea is to fill the bottom-right cell with the maximum value from its left and upper cells.
Then, fill the remaining cells with the maximum value from the left and upper cells, but also, only if the corresponding cell is greater than the left and upper cell.

This is how the code would look like:

```python
def maxAverageOfPath(mat):
    N = len(mat)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = mat[0][0]
    for i in range(N):
        for j in range(N):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + mat[i][j]
            elif i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + mat[i][j]
            elif i != 0 and j != 0:
                dp[i][j] = mat[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    return float(dp[-1][-1]) / (N * N)
```

This code fills the bottom-right cell with the maximum value from its left and upper cells.
Then, it fills the remaining cells with the maximum value from the left and upper cells, but also, only if the corresponding cell is greater than the left and upper cell.

The time complexity of this algorithm is O(N^2), as it iterates over each cell of the matrix exactly once.
The space complexity is also O(N^2), as it creates a new matrix to store the maximum cost at each cell.

The above algorithm returns the maximum average of all the paths.

This algorithm can be easily extended to handle any square matrix of any size.

Here are some more details about the solution:

- The idea is to fill the bottom-right cell with the maximum value from its left and upper cells.
- Then, fill the remaining cells with the maximum value from the left and upper cells, but also, only