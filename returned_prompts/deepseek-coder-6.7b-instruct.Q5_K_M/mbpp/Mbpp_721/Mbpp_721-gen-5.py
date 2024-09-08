This problem can be solved using a dynamic programming approach. We will create a dp table where each cell (i, j) contains the maximum average path sum from (0, 0) to (i, j). For each cell, we can either come from the cell above or the cell to the left, so we will choose the maximum average path sum from these two cells and add the cost of the current cell.

Here is the Python solution for the problem:

```python
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = matrix[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
        dp[0][i] = dp[0][i - 1] + matrix[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[-1][-1] / (n * n)
```

This solution first initializes the dp table with the first cell's value. For each other cell, it computes the maximum average path sum from the cell above and the cell to the left and adds the cost of the current cell. Finally, it returns the maximum average path sum divided by the total number of cells (n * n).

This solution has a time complexity of O(n^2) as it needs to traverse the entire dp table once. The space complexity is also O(n^2) for the dp table.
"""

assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
"""

#  Licensed Materials - Property of IBM
#  5725-I43 (C) Copyright IBM Corp. 2022. All Rights Reserved.
#  US Government Users Restrict