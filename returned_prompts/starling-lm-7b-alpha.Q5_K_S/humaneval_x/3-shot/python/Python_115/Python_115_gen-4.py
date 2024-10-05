    def dfs(grid, row, col, capacity):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        result = 0
        result = max(result, dfs(grid, row + 1, col, capacity), dfs(grid, row - 1, col, capacity),
                     dfs(grid, row, col + 1, capacity), dfs(grid, row, col - 1, capacity))
        result += 1
        return result if result % capacity == 0 else result // capacity + 1

    return dfs(grid, len(grid) // 2, len(grid[0]) // 2, capacity)


