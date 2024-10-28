```
def maxAverageOfPath(cost):
    N = len(cost)
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][0] = cost[i][0]
        dp[0][i] = cost[0][i]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = cost[i][j] + max(dp[i-1][j], dp[i][j-1])
    max_path_sum = 0
    for i in range(N):
        for j in range(N):
            path_sum = dp[i][j]
            path_length = i + j + 1
            max_path_sum = max(max_path_sum, path_sum / path_length)
    return max_path_sum
```  