def sort_matrix(matrix):
    return [list(i) for i in sorted([[sum(row), row] for row in matrix])][1:]