
def minPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    N = len(grid)
    dp = [[[float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, N + 1):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j][k] = min(dp[i - 1][j][k - 1] + grid[i][j], dp[i][j][k])
                    dp[i][j][k] = min(dp[i][j - 1][k - 1] + grid[i][j], dp[i][j][k])
                    dp[i][j][k] = min(dp[i - 1][j - 1][k - 2] + grid[i][j], dp[i][j][k])
    result = []
    for i in range(N):
        for j in range(N):
            for k in range(1, N + 1):
                if dp[i][j][k] == dp[i][j][k - 1] + grid[i][j]:
                    result.append(grid[i][j])
                    break
    return result



