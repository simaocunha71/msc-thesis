
    class Solution:
        def minPath(self, grid, k):
            N = len(grid)
            if N == 1:
                return grid[0]
            dp = [[-1] * N for _ in range(N)]
            for i in range(N):
                dp[i][0] = grid[i][0]
            for j in range(N):
                dp[0][j] = grid[0][j]
            for i in range(1, N):
                for j in range(1, N):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + grid[i][j]
            def dfs(i, j, k, dp, grid, s, path):
                if i == N - 1 and j == N - 1 and k == 0:
                    path.append(dp[i][j])
                    return
                if i == N - 1 or j == N - 1 or dp[i][j] > dp[i-1][j-1]:
                    dfs(i, j, k, dp, grid, s, path)
                else:
                    dfs(i-1, j, k-1, dp, grid, s + grid[i][j], path)
            path = []
            dfs(N-1, N-1, k, dp, grid, 0, path)
            return path

```