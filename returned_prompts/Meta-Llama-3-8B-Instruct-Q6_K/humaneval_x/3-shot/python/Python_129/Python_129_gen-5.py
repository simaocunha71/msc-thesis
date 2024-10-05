    def dfs(grid, k, row, col, path, visited):
        if k == 0:
            return path
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + x, col + y
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                new_path = dfs(grid, k - 1, new_row, new_col, path + [grid[new_row][new_col]], visited)
                if new_path:
                    return new_path
                visited.remove((new_row, new_col))
        return None

    min_path = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = dfs(grid, k, i, j, [grid[i][j]], {(i, j)})
            if path and (min_path is None or path < min_path):
                min_path = path
    return min_path


