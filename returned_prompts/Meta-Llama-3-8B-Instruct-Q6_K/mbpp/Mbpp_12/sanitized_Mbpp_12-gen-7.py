def sort_matrix(matrix):
    return [i for _, i in sorted(((sum(row), row) for row in matrix))]
    # or return sorted(matrix, key=sum)