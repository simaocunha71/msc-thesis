
def maxAverageOfPath(matrix: list) -> float:
    dp = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != 0 and j != 0:
                dp = max(dp, matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] + matrix[i-1][j-1],)
    return dp / (len(matrix) * len(matrix[0]))


