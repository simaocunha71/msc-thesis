    def dfs(grid, k, x, y):
        n = len(grid)
        if k == 1:
            return [grid[x][y]]
        if grid[x][y] > n:
            return []
        result = []
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            result.extend(dfs(grid, k - 1, x + dx, y + dy))
        result.append(grid[x][y])
        return sorted(result)

    return dfs(grid, k, 0, 0)


