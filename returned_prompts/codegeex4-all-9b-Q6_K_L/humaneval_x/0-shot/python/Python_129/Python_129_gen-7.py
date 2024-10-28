def minPath(grid, k):
    n = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * n for _ in range(n)]
    min_path = []

    def dfs(x, y, path, steps):
        nonlocal min_path
        if steps == k:
            if not min_path or path < min_path:
                min_path = path
            return
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                dfs(nx, ny, path + [grid[nx][ny]], steps + 1)
        visited[x][y] = False

    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]], 1)

    return min_path

print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3)) # [1, 2, 1]
print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1)) # [1]