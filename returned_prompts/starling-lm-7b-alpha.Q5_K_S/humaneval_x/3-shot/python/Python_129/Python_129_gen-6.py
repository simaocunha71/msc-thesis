    def valid(grid, row, col, n):
        return row >= 0 and row < n and col >= 0 and col < n

    def minPath(grid, k):
        n = len(grid)
        min_grid = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            min_grid[i][i] = grid[i][i]
        for length in range(2, k + 1):
            for row in range(n):
                for col in range(n):
                    if length == 2:
                        min_grid[row][col] = grid[row][col] + min_grid[row][col - 1]
                        min_grid[row][col] = min(min_grid[row][col], grid[row][col] + min_grid[row - 1][col])
                    if not valid(grid, row, col - 1, n):
                        continue
                    if not valid(grid, row, col + 1, n):
                        continue
                    if not valid(grid, row - 1, col, n):
                        continue
                    if not valid(grid, row + 1, col, n):
                        continue
                    min_grid[row][col] = grid[row][col] + min(min_grid[row][col - 1], min_grid[row - 1][col], min_grid[row + 1][col], min_grid[row][col + 1])
        path = []
        curr_row, curr_col = 0, 0
        curr_val = min_grid[curr_row][curr_col]
        while k:
            path.append(grid[curr_row][curr_col])
            k -= 1
            if curr_col > 0:
                val_left = grid[curr_row][curr_col - 1] + min_grid[curr_row][curr_col - 1] - curr_val
            else:
                val_left = float('inf')
            if curr_row > 0:
                val_up = grid[