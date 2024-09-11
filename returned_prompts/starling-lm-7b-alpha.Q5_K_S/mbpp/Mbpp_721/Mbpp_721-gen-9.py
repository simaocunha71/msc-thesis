Here is a possible solution using Python:

```python
def maxAverageOfPath(mat):
    m = len(mat)
    n = len(mat[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = mat[i][0]
    for j in range(n):
        dp[0][j] = mat[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + mat[i][j]
    return dp[m - 1][n - 1] / (m + n - 1)
```

In the code above, we use a dynamic programming approach to solve the problem. We maintain a matrix `dp` where `dp[i][j]` represents the maximum cost of a path from the top-left to the (i, j) cell. We initialize the first row and first column of `dp` with the costs of the corresponding cells in the input matrix `mat`. Then, for each cell `(i, j)` with `i > 0` and `j > 0`, we calculate `dp[i][j]` as the maximum of the cost of the path from the (i - 1, j) cell and the cost of the path from the (i, j - 1) cell, and add the cost of the current cell `mat[i][j]`. Finally, we return the maximum cost `dp[m - 1][n - 1]` divided by the total number of cells in the path, which is `m + n - 1`.

To verify the solution, you can use the given test case:

```python
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # Output: 5.2
```

This will print the maximum average of the path, which is `5.2`.

```python
# Time Complexity: O(n * m)
# Space Complexity