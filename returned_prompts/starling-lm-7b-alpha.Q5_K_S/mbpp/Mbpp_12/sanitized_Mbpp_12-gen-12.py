def sort_matrix(matrix):
    matrix = sorted(matrix, key=sum, reverse=True)
    return matrix