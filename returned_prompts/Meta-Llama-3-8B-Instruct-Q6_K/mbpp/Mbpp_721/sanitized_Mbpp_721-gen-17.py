def maxAverageOfPath(cost):
    N = len(cost)
    dp = [[0.0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][0] = cost[i][0]
    for j in range(N):
        dp[0][j] = cost[0][j]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = cost[i][j] + max(dp[i-1][j], dp[i][j-1]) / (i+j)
    return max(dp[-1])