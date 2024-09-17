def maxAverageOfPath(cost):
    rows, cols = len(cost), len(cost[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = cost[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    max_sum = float('-inf')
    for i in range(rows):
        for j in range(cols):
            path_sum = dp[i][j]
            path_len = i + j
            max_sum = max(max_sum, path_sum / path_len)
    return max_sum