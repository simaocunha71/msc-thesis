def sort_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i].sort()
    matrix.sort(key = sum)
    return matrix