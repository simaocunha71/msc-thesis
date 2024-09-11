```
# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maxAverageOfPath(self, path):
        """
        :type path: List[List[int]]
        :rtype: float
        """
        dp = [0]*len(path)
        for i in xrange(len(path)):
            dp[i] = path[i][0]
        for j in xrange(1, len(path)):
            dp[j] += path[j][j]
            for i in reversed(xrange(j)):
                dp[i] = max(path[i][j]+dp[i+1], path[j][i]+dp[i])
        return float(dp[0]) / (1+len(path))

```

```
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def maxAverageOfPath(self, path):
        """
        :type path: List[List[int]]
        :rtype: float
        """
        def max_sum_of_path(path, i, j, lookup):
            if i > j:
                return 0
            if i == j:
                return path[i][j]
            if lookup[i][j]:
                return lookup[i][j]
            lookup[i][j] = max(path[i][j] + max_sum_of_path(path, i+1, j, lookup),
                               path[i][j] + max_sum_of_path(path, i, j-1, lookup))
            return lookup[i][j]

        return float(max_sum_of_path(path, 0, len(path)-1, [[False]*len(path) for _ in xrange(len(path))])) / (1+len(path))

```
```

```
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def maxAverageOfPath(self, path):
        """
        :type path: List[List[int]]