```
# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def maxAverageOfPath(self, path):
        """
        :type path: List[List[int]]
        :rtype: float
        """
        M = len(path)
        N = len(path[0])
        dp = [[0]*N for _ in xrange(M)]
        for i in xrange(M):
            for j in xrange(N):
                if i == 0 and j == 0:
                    dp[i][j] = path[i][j]
                elif i == 0:
                    dp[i][j] = path[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = path[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = path[i][j] + max(dp[i-1][j], dp[i][j-1])
        return float(dp[M-1][N-1]) / ((M-1)+(N-1)+1)

```
