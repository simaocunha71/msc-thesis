    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    moves = [(0, 1), (1, 0)]

    for k in range(1, len(grid) * len(grid)):
        new