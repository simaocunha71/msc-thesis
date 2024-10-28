    def dfs(grid, k, visited, x, y, path, result):
        if len(path) == k:
            result.append(path)
            return
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return
        if (x, y) in visited or grid[x][y] < 1 or grid[x][y] > len(grid) * len(grid[0]):
            return
        if (x, y) in path:
            return
        visited.add((x, y))
        path.append(grid[x][y])
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(grid, k, visited, x + dx, y + dy, path, result)
        visited.remove((x, y))
        path.pop()

    result = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(grid, k, visited, i, j, [], result)

    result.sort()
    return [v for v, _ in result]


