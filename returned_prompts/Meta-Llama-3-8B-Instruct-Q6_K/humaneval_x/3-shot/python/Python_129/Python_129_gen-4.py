    def dfs(i, j, path, visited, k):
        if k == 0:
            return [path]
        if (i, j) in visited:
            return []
        visited.add((i, j))
        paths = []
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                paths.extend(dfs(x, y, path + [grid[x][y]], visited, k-1))
        visited.remove((i, j))
        return paths

    min_path = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            paths = dfs(i, j, [grid[i][j]], set(), k)
            if not min_path or paths < min_path:
                min_path = paths
    return min_path[0]


