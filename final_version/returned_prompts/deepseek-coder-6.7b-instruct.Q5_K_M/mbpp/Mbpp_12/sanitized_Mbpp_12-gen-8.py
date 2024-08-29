def sort_matrix(matrix):
    sum_rows = [sum(row) for row in matrix]
    return [row for _, row in sorted(zip(sum_rows, matrix))]