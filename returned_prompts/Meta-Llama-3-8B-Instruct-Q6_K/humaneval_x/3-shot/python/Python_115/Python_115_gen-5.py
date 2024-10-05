    def max_fill(grid, capacity):
        m, n, total = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
        if total % capacity == 0:
            return total // capacity
        else:
            return total // capacity + 1


