def sort_matrix(matrix):
    sums = [sum(row) for row in matrix]
    return [row for _, row in sorted(zip(sums, matrix))]