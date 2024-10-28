
class Solution:
    def smallest_change(self, arr):
        # Write your code here
        n = len(arr)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = 0
            for j in range(i+1, n+1):
                dp[i][j] = 10**9
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)
        return dp[1][n]

