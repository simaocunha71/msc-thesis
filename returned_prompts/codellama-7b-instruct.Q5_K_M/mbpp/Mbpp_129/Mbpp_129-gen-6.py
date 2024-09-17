
def magic_square_test(matrix: list) -> bool:
    matrix_sum = sum(sum(row) for row in matrix)
    if matrix_sum % 2 == 1:
        return False

    matrix_size = len(matrix)
    mid = matrix_size // 2

    diagonal_sum = sum(matrix[i][i] for i in range(matrix_size))
    if diagonal_sum != matrix_sum // 2:
        return False

    anti_diagonal_sum = sum(matrix[i][matrix_size - i - 1] for i in range(matrix_size))
    if anti_diagonal_sum != matrix_sum // 2:
        return False

    for i in range(matrix_size):
        row_sum = sum(matrix[i])
        if row_sum != matrix_sum // matrix_size:
            return False

        col_sum = sum(matrix[j][i] for j in range(matrix_size))
        if col_sum != matrix_sum // matrix_size:
            return False

    return True

