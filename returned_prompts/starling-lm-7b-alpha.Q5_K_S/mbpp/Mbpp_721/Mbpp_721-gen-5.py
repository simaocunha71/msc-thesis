
def maxAverageOfPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        matrix[i][0] += matrix[i-1][0] if i > 0 else 0
    for j in range(1,n):
        matrix[0][j] += matrix[0][j-1]
    for i in range(1,m):
        for j in range(1,n):
            matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])
    return matrix[m-1][n-1] / (m + n - 1)


