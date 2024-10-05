def minPath(grid, k):
    n = len(grid)
    dp = [[None] * (k + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][0] = [grid[i][j]]
    for l in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if dp[i][l - 1] is None:
                    continue
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n and dp[x][y] is not None:
                        new_path = dp[i][l - 1] + [grid[x][y]]
                        if dp[x][y] is None or (len(dp[x][y]) == len(new_path) and new_path < dp[x][y]) or (len(dp[x][y]) < len(new_path)):
                            dp[x][y] = new_path
    min_path = None
    for path in dp:
        for p in path:
            if p is not None and (min_path is None or len(p) < len(min_path) or (len(p) == len(min_path) and p < min_path)):
                min_path = p
    return min_path