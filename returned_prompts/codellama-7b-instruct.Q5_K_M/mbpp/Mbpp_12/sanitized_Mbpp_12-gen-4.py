def sort_matrix(matrix):
    return [[*row] for row in sorted(matrix, key=sum)]