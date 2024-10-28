
    def minPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        N = len(grid)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            dp[i][i] = grid[i][i]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + grid[i][j]
        ans = []
        for i in range(N):
            for j in range(i, N):
                if dp[i][j] == k:
                    ans = grid[i][j]
        return ans


class Solution:
    def minPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        N = len(grid)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            dp[i][i] = grid[i][i]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + grid[i][j]
        ans = []
        for i in range(N):
            for j in range(i, N):
                if dp[i][j] == k:
                    ans = grid[i][j]
        return ans
