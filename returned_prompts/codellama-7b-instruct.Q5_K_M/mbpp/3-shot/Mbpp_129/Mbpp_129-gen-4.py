
def magic_square_test(matrix: list):
    sum_rows = [sum(row) for row in matrix]
    sum_cols = [sum(col) for col in zip(*matrix)]
    if sum(sum_rows) != sum(sum_cols):
        return False
    sum_diag = sum(matrix[i][i] for i in range(len(matrix)))
    if sum_diag != sum(sum_rows) or sum_diag != sum(sum_cols):
        return False
    return True


