    def find_min_path(grid, row, col, k, visited, result):
        if k == 0:
            return

        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return

        if k == 1:
            result.append(grid[row][col])
            return

        visited[row][col] = True

        find_min_path(grid, row - 1, col, k - 1, visited, result)
        find_min_path(grid, row, col - 1, k - 1, visited, result)
        find_min_path(grid, row + 1, col, k - 1, visited, result)
        find_min_path(grid, row, col + 1, k - 1, visited, result)

        visited[row][col] = False

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = []
    find_min_path(grid, 0, 0, k, visited, result)
    return result
