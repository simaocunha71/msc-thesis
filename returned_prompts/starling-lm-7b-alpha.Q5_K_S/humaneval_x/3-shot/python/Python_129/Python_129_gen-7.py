    def dfs(i, j, current_path, visited, grid, k, result):
        current_path.append(grid[i][j])
        visited[i][j] = True
        if len(current_path) == k:
            result[0] = current_path
            return

        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if 0 <= new_i < rows and 0 <= new_j < cols and not visited[new_i][new_j]:
                dfs(new_i, new_j, current_path.copy(), visited.copy(), grid, k, result)

        visited[i][j] = False
        current_path.pop()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    result = [None]
    dfs(0, 0, [grid[0][0]], [[False] * cols for _ in range(rows)], grid, k, result)
    return result[0]


