    def dfs(x, y, k):
        if k == 0:
            return [grid[x][y]]

        result = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                result += dfs(nx, ny, k - 1)

        return result

    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                result = dfs(i, j, k)
                break
        if result:
            break

    return sorted(result, key=lambda x: (grid[x[0]][x[1]], x[2], x[3], x[4]))


