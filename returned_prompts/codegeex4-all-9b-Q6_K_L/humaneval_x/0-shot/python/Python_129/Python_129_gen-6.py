```python

def minPath(grid, k):
    n = len(grid)
    min_val = float('inf')
    min_path = []
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            visited = set([(i, j)])
            if dfs(grid, i, j, path, visited, k):
                if sum(path) < min_val:
                    min_val = sum(path)
                    min_path = path
    return min_path

def dfs(grid, i, j, path, visited, k):
    if len(path) == k:
        return True
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
            path.append(grid[ni][nj])
            visited.add((ni, nj))
            if dfs(grid, ni, nj, path, visited, k):
                return True
            path.pop()
            visited.remove((ni, nj))
    return False
```
