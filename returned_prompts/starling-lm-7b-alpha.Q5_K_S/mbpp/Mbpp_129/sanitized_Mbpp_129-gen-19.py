def magic_square_test(matrix: list) -> bool:
    matrix_sum = sum(matrix)
    if matrix_sum % 15 != 0:
        return False
    row_sum = sum(matrix[0])
    col_sum = sum(matrix[i][0] for i in range(len(matrix)))
    diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
    diag_sum2 = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    if not (row_sum == col_sum == diag_sum == diag_sum2 == matrix_sum / 15):
        return False
    return True