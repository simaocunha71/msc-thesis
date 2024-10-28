    # N = len(grid[0])
    # dp = [[0] * N for _ in range(N)]

    # for i in range(N):
    #     dp[i][i] = grid[i][i]

    # for i in range(N - 1):
    #     for j in range(i + 1, N):
    #         dp[i][j] = min(dp[i][j - 1], dp[i + 1][j], dp[i][j - 1] + grid[i][j], dp[i + 1][j] + grid[i][j])

    # return [dp[0][k - 1] for k in range(1, N)]

    N = len(grid)
    dp = [0] * N

    for i in range(N):
        dp[i] = grid[i][0]

    for i in range(1, N):
        for j in range(i, N):
            dp[j] = min(dp[j], dp[j - 1], dp[j] + grid[j][i], dp[j - 1] + grid[j][i])

    return [dp[k - 1] for k in range(1, N)]
