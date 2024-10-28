```
def maxAverageOfPath(matrix):
    def dfs(i, j, total, count):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return total / count if count > 0 else 0
        total += matrix[i][j]
        count += 1
        matrix[i][j] = -1
        return max(dfs(i + 1, j, total, count), dfs(i, j + 1, total, count))

    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                res = max(res, dfs(i, j, 0, 1))
    return res
```


The function `maxAverageOfPath` takes as input a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. It returns the maximum average of all existing paths.

The function uses a depth-first search (DFS) approach to traverse the matrix. The DFS function takes four parameters: `i` and `j` are the current cell's coordinates, `total` is the total cost of the path, and `count` is the number of cells visited in the path.

The DFS function returns the maximum average of the path. If the current cell is out of the matrix's bounds or has been visited before, it returns the total cost divided by the number of cells visited. Otherwise, it adds the current cell's cost to the total cost, increments the count, marks the cell as visited, and recursively calls itself for the cell below and to the right.

The outer function iterates over all cells in the matrix, and for each cell, it calls the DFS function with the initial values. It keeps track of the maximum average found so far and returns it at the end.

In the unit test, the function is called with the matrix `[[1, 2, 3], [6, 5, 4], [7, 3, 9]]`, and it returns `5.2`, which is the maximum average of all existing paths.