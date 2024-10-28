from typing import List
def maxAverageOfPath(grid: List[List[int]]) -> float:
    N = len(grid)
    memo = [[0.0]*N for _ in range(N)]
    memo[0][0] = grid[0][0]
    for i in range(1, N):
        memo[i][0] = memo[i-1][0] + grid[i][0]
    for j in range(1, N):
        memo[0][j] = memo[0][j-1] + grid[0][j]
    for i in range(1, N):
        for j in range(1, N):
            memo[i][j] = max(memo[i-1][j], memo[i][j-1]) + grid[i][j]
    max_avg = 0.0
    for i in range(N):
        for j in range(N):
            avg = memo[i][j] / (i+1)
            max_avg = max(max_avg, avg)
    return max_avg