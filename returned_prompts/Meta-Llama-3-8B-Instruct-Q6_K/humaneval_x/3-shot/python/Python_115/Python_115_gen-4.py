    def max_fill(grid, capacity):
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                res += min(grid[i][j], capacity)
        return res
    return max_fill(grid, capacity)


