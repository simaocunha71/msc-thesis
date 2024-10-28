    def find_min_path(grid, k, row, col, visited, path):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            if k == 0:
                return path
            else:
                return []

        if k == 0:
            return path
        elif row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or visited[row][col]:
            return []
        elif grid[row][col] <= k:
            visited[row][col] = True
            path.append(grid[row][col])
            k -= grid[row][col]
            new_path = find_min_path(grid, k, row - 1, col, visited, path)
            if new_path:
                return new_path
            new_path = find_min_path(grid, k, row + 1, col, visited, path)
            if new_path:
                return new_path
            new_path = find_min_path(grid, k, row, col - 1, visited, path)
            if new_path:
                return new_path
            new_path = find_min_path(grid, k, row, col + 1, visited, path)
            if new_path:
                return new_path
            return []
        else:
            return []

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    result = find_min_path(grid, k, 0, 0, visited, [])
    result.sort()
    return result


