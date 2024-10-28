    def dfs(i, j, k, grid, visited):
        if k == 0:
            return []
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return []
        if visited[i][j] or grid[i][j] == 0:
            return []

        visited[i][j] = True
        res = []
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            res += dfs(i + direction[0], j + direction[1], k - 1, grid, visited)
        if res:
            res.append(grid[i][j])
        visited[i][j] = False
        return res

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return dfs(0, 0, k, grid, visited)
}



