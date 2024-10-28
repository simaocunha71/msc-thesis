This problem can be solved by using dynamic programming. We can define a 2D array dp where dp[i][j] represents the minimum path of length k that starts from cell (i, j). The base case is dp[i][j] = grid[i][j] when k = 1.

For k > 1, we can compute dp[i][j] by considering all possible previous cells that can reach cell (i, j). Let (x, y) be a previous cell, then the cost of reaching cell (i, j) from (x, y) is dp[x][y] + grid[i][j]. We can take the minimum of all these costs to get dp[i][j].

To find the minimum path of length k, we can iterate over all cells (i, j) and take the minimum of dp[i][j] for all i, j.

Here is the implementation in Python:

```python
def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = grid[i][j]
    for l in range(2, k+1):
        for i in range(n):
            for j in range(n):
                for x in range(max(0, i-l+1), min(n, i+1)):
                    for y in range(max(0, j-l+1), min(n, j+1)):
                        if i != x or j != y:
                            dp[i][j] = min(dp[i][j], dp[x][y] + grid[i][j])
    min_path = float('inf')
    for i in range(n):
        for j in range(n):
            min_path = min(min_path, dp[i][j])
    return min_path
```

The time complexity of this solution is O(k * n^4) and the space complexity is O(n^2).