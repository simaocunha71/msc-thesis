    def path(cell):
        return [cell[0], cell[1], cell[0]]

    def compare(path1, path2):
        for idx, (elem1, elem2) in enumerate(zip(path1, path2)):
            if elem1 != elem2:
                return idx, elem1 < elem2
        return 10 ** 9, path1 < path2

    def dfs(cell, visited, path, k, grid, idx, idx2):
        if idx == k:
            path.append(cell)
            return True
        if idx2 >= len(grid) or idx2 < 0:
            return False
        if cell[0] == cell[1]:
            if visited[idx2 * len(grid) + cell[0]]:
                return dfs(cell, visited, path, k, grid, idx, idx2 + 1)
            visited[idx2 * len(grid) + cell[0]] = True
            if dfs(cell, visited, path, k, grid, idx, idx2 + 1):
                path.append(cell)
                return True
            return False
        if visited[idx2 * len(grid) + cell[0]]:
            return dfs(cell, visited, path, k, grid, idx, idx2 + 1)
        if visited[idx2 * len(grid) + cell[1]]:
            return dfs(cell, visited, path, k, grid, idx, idx2 + 1)
        visited[idx2 * len(grid) + cell[0]] = True
        visited[idx2 * len(grid) + cell[1]] = True
        path.append(cell)
        res = dfs(cell, visited, path, k, grid, idx, idx2 + 1)
        if res:
            return True
        path.pop()
        res = dfs(cell, visited, path, k, grid, idx, idx2 + 1)
        return res

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    min_path = []
    for i in range(len(grid) * len