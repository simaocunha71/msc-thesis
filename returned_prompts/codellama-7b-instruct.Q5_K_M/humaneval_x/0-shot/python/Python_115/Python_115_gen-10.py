
    # O(N)
    def max_fill(grid, capacity):
        N = len(grid)
        M = len(grid[0])
        dp = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        for i in range(1, N):
            for j in range(M):
                if grid[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j]) + 1
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
        return sum(dp[-1])

