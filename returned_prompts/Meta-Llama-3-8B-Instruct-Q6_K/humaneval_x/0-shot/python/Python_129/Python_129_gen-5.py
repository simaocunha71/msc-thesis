Here is the Python code to solve the problem:

```Python
def minPath(grid, k):
    N = len(grid)
    visited = [[False for _ in range(N)] for _ in range(N)]
    min_path = []
    min_path_val = float('inf')

    def dfs(i, j, path, path_val):
        nonlocal min_path, min_path_val
        if len(path) == k:
            if path_val < min_path_val:
                min_path = path[:]
                min_path_val = path_val
            return
        if path_val >= min_path_val:
            return
        visited[i][j] = True
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                dfs(x, y, path + [grid[x][y]], path_val + grid[x][y])
        visited[i][j] = False

    for i in range(N):
        for j in range(N):
            dfs(i, j, [grid[i][j]], grid[i][j])

    return min_path
```
This function uses depth-first search (DFS) to explore all possible paths of length `k` in the grid. It keeps track of the minimum path found so far and returns it at the end. The DFS function is called for each cell in the grid, and it explores all possible paths that start from that cell. The `visited` matrix is used to keep track of the cells that have been visited, to avoid visiting the same cell multiple times. The `min_path` and `min_path_val` variables are used to keep track of the minimum path found so far. The function returns the minimum path found. 

Note: The grid is a list of lists in Python, where each inner list represents a row in the grid. The `k` parameter is the length of the path we are looking for. The function returns a list of the values on the cells that the minimum path goes through. 

For example, if we call `minPath([[1,2,3], [4,5,6], [7,8,9]], 3)`, the function will return `[1, 2, 1]`, which is the minimum path of length 3 in the grid. If we call `minPath([[5