def sort_matrix(matrix):
    rows = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    row_sums = [sum(row) for row in rows]
    sorted_rows = sorted(rows, key=lambda row: row_sums.index(sum(row)))
    return [sorted_rows[i] for i in range(len(matrix))]