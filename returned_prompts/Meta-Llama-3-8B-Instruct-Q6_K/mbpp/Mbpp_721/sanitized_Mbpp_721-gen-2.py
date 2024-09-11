from typing import List
def maxAverageOfPath(matrix: List[List[int]]) -> float:
    N = len(matrix)
    memo = [[0.0] * N for _ in range(N)]
    memo[0][0] = matrix[0][0]
    for i in range(1, N):
        memo[i][0] = memo[i-1][0] + matrix[i][0]
    for j in range(1, N):
        memo[0][j] = memo[0][j-1] + matrix[0][j]
    for i in range(1, N):
        for j in range(1, N):
            memo[i][j] = max(memo[i-1][j], memo[i][j-1]) + matrix[i][j]
    max_sum = memo[N-1][N-1]
    for i in range(N):
        for j in range(N):
            max_sum = max(max_sum, memo[i][j])
    return max_sum / (N*N)  # Total sum divided by the number of cells visited in the path. 
    # The maximum average is the maximum sum divided by the number of cells visited in the path.  #