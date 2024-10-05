    def dfs(i, j, k, path):
        if k == 0:
            return path
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] not in path:
                    grid[ni][nj] = None
                    res = dfs(ni, nj, k-1, path + [grid[ni][nj]])
                    if res:
                        return res
        return None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in [x for row in grid for x in row]:
                grid[i][j] = None
                path = dfs(i, j, k, [grid[i][j]])
                if path:
                    return path

    return None


