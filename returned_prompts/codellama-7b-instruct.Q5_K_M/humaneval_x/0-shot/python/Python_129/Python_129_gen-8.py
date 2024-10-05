
def minPath(grid, k):
    # Write your code here
    N = len(grid)
    dp = [[[float('inf') for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][0] = grid[i][j]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if k == 0:
                    dp[i][j][k] = grid[i][j]
                else:
                    for p in range(N):
                        if i - p < 0 or j - p < 0 or i + p >= N or j + p >= N:
                            continue
                        dp[i][j][k] = min(dp[i][j][k], dp[i - p][j - p][k - 1] + grid[i][j])
    res = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dp[i][j][k] < float('inf'):
                    res.append(grid[i][j])
    return sorted(res)
