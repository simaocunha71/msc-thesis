def maxAverageOfPath(matrix):
    N = len(matrix)
    max_sum = [0] * N
    max_sum[N - 1] = matrix[N - 1][N - 1]
    for i in reversed(range(N - 1)):
        max_sum[i] = max(max_sum[i + 1], matrix[i][N - 1])
    for i in reversed(range(N - 1)):
        for j in reversed(range(N - 1)):
            max_sum[j] = max(max_sum[j], max_sum[j + 1] + matrix[i][j])
    return max_sum[0] / (N * N)