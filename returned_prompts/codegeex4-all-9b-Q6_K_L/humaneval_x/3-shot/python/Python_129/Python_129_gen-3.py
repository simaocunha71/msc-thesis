    def dfs(x, y, k, grid, memo):
        if k == 0:
            return [grid[x][y]]
        if (x, y, k) in memo:
            return memo[(x, y, k)]
        result = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] not in result:
                result.append(grid[nx][ny])
        for r in result:
            grid[x][y] = r
            temp = dfs(nx, ny, k-1, grid, memo)
            if temp:
                memo[(x, y, k)] = [grid[x][y]] + temp
                return memo[(x, y, k)]
        return None

    for i in range(len(grid)):
        for j in range(len(grid)):
            for k in range(1, len(grid) * len(grid) + 1):
                if dfs(i, j, k, grid, {}):
                    return dfs(i, j, k, grid, {})
    return None