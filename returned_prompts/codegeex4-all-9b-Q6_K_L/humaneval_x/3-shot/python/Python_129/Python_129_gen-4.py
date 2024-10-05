    n = len(grid)
    visited = set()
    min_path = []

    def dfs(x, y, k, path):
        nonlocal min_path
        if k == 0:
            if not min_path or path < min_path:
                min_path = path
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                dfs(nx, ny, k - 1, path + [grid[nx][ny]])

    for i in range(n):
        for j in range(n):
            dfs(i, j, k, [grid[i][j]])
    return min_path

