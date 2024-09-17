def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0.0] * n for _ in range(n)]
    dp[0][0] = cost[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    max_avg = 0.0
    for i in range(1, n):
        for j in range(1, n):
            avg = dp[i][j] / (i + j)
            max_avg = max(max_avg, avg)
    return max_avg