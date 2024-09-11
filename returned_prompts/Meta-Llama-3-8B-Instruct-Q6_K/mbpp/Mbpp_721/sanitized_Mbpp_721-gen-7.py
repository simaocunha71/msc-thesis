from typing import List
def maxAverageOfPath(matrix: List[List[int]]) -> float:
    N = len(matrix)
    dp = [[0.0] * N for _ in range(N)]
    dp[0][0] = matrix[0][0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    max_sum = dp[N-1][N-1]
    max_len = N*N
    for i in range(N):
        for j in range(N):
            path_sum = dp[i][j]
            path_len = i + j
            if path_sum > max_sum or (path_sum == max_sum and path_len < max_len):
                max_sum = path_sum
                max_len = path_len
    return max_sum / max_len