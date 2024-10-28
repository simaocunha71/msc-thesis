    def minpath(grid, k, x, y, path, visited):
        if len(path) == k:
            return path

        minpath = path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[ny * n + nx]:
                minpath = min(minpath, minpath(grid, k, nx, ny, path + [grid[ny][nx]], visited.copy(
                ) & ~(ny * n + nx)))

        return minpath

    n = len(grid)
    visited = [True] * (n * n)
    visited[0] = False
    return minpath(grid, k, 0, 0, [grid[0][0]], visited)


