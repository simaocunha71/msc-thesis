def maxAverageOfPath(matrix: list) -> float:
    N = len(matrix)
    total = 0
    for i in range(N):
        total += matrix[i][i]
    return total / N