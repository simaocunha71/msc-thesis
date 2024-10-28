
    def max_fill(grid, capacity):
        import math
        m, n = len(grid), len(grid[0])
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for k in range(j, n):
                    dp[i+1] = max(dp[i+1], dp[i] + min(capacity, grid[i][k]) * (k - j + 1))
        return dp[m]
