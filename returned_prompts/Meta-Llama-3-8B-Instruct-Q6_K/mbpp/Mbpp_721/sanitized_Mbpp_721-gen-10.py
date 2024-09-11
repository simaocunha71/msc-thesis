from typing import List
import numpy as np
def maxAverageOfPath(cost: List[List[int]]) -> float:
    N = len(cost)
    dp = [[0.0] * N for _ in range(N)]
    dp[0][0] = cost[0][0]
    for i in range(N):
        for j in range(N):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] += cost[i][j]
    max_path = 0
    for i in range(N):
        for j in range(N):
            path_sum = dp[i][j]
            path_len = i + j
            path_avg = path_sum / path_len
            max_path = max(max_path, path_avg)
    return max_path