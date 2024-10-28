def maxAverageOfPath(cost):
    N = len(cost)
    memo = [[0.0] * N for _ in range(N)]
    for i in range(N):
        memo[i][0] = cost[i][0]
        for j in range(1, N):
            memo[i][j] = cost[i][j] + max(memo[i][j-1], memo[i-1][j])
    max_sum = memo[N-1][N-1]
    for i in range(N):
        for j in range(N):
            path_sum = memo[i][j]
            path_length = i * N + j
            if i > 0:
                path_sum -= memo[i-1][j]
                path_length -= N
            if j > 0:
                path_sum -= memo[i][j-1]
                path_length -= 1
            max_sum = max(max_sum, path_sum / path_length)
    return max_sum