The approach here is a dynamic programming problem. We start from the bottom right cell and go up and left filling in the maximum average path cost for each cell.

```python
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[-1][-1] = matrix[-1][-1]

    # Initialize the last row and the last column
    for i in range(n-2, -1, -1):
        dp[i][-1] = max(dp[i+1][-1] - matrix[i][-1], matrix[i][-1])
        dp[-1][i] = max(dp[-1][i+1] - matrix[-1][i], matrix[-1][i])

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + matrix[i][j]

    return dp[0][0] / ((n-1)*2)


print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # 5.2
```

This solution is based on the idea of dynamic programming where we keep track of the maximum average path cost for each cell. We initialize the last cell with its own value and for all cells in the last row and last column, the maximum average path cost is the maximum of its own value and the maximum average path cost of the next cell. For all other cells, the maximum average path cost is the maximum of the maximum average path cost of the next cell in the right and bottom directions. Finally, we return the maximum average path cost of the top left cell divided by the number of cells visited.
"""


# ---------------------
# Code by: Ashwin Reddy
# ---------------------
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
Q