
def maxAverageOfPath(matrix: list) -> float:
    m = len(matrix)
    n = len(matrix[0])
    if m > n:
        m, n = n, m
    for i in range(m):
        for j in range(n):
            matrix[i][j] += (i+j)
    matrix.insert(0, [0] * n)
    for i in range(1, m+1):
        matrix.insert(0, [0] * n)
    return max(matrix[i][j] / (i + j) for i in range(m+1) for j in range(n+1))


