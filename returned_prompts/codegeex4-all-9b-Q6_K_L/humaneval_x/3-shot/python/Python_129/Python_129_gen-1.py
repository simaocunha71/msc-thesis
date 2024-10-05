    def dfs(i, j, k, visited):
        if k == 0:
            return [grid[i][j]]

        if (i, j) in visited:
            return None

        visited.add((i, j))

        min_path = None

        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid):
                path = dfs(ni, nj, k-1, visited)
                if path:
                    if min_path is None or path[0] < min_path[0]:
                        min_path = path

        visited.remove((i, j))

        return [grid[i][j]] + min_path if min_path else None

    min_path = None

    for i in range(len(grid)):
        for j in range(len(grid)):
            path = dfs(i, j, k-1, set())
            if path:
                if min_path is None or path[0] < min_path[0]:
                    min_path = path

    return min_path

