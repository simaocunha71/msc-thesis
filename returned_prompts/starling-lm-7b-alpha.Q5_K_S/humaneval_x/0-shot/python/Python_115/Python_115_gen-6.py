
We can use DP (dynamic programming) to solve this problem.

The idea is to use the bottom-up approach to solve this problem.
For each cell in the grid, we calculate the minimum number of times to fill the well with the given capacity.

Here are the steps to solve the problem:
1. Create a DP array to store the minimum number of times to fill each cell in the grid.
2. Use the bottom-up approach to fill each cell in the grid. For each cell, we use the given capacity to fill the cell and then update the DP array.
3. Finally, we calculate the total number of times to fill all the cells in the grid by adding the minimum number of times to fill each cell.

Here are the detailed steps to solve the problem:

1. Initialize the DP array with the size of the grid and the given capacity.
2. For each cell in the grid, we calculate the minimum number of times to fill the cell by dividing the capacity of the cell by the given capacity.
3. Update the DP array for each cell by adding the minimum number of times to fill the cell.
4. Finally, we calculate the total number of times to fill all the cells in the grid by adding the minimum number of times to fill each cell.

Here is the detailed code to solve the problem:

```python
def max_fill(grid, capacity):
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            cnt = grid[i][j]
            dp[i+1][j+1] = (cnt + capacity - 1) // capacity
            dp[i+1][j+1] += dp[i+1][j]
            dp[i+1][j+1] += dp[i][j+1]
            dp[i+1][j+1] -= dp[i][j]
    return dp[n][m]
```

This is the detailed solution to the problem.

The time complexity of this solution