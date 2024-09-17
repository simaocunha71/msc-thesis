
def magic_square_test(matrix: list) -> bool:

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return False

    size = rows

    sum_of_rows = [sum(row) for row in matrix]
    sum_of_cols = [sum(col) for col in zip(*matrix)]
    diag1 = sum(matrix[i][i] for i in range(size))
    diag2 = sum(matrix[i][size - i - 1] for i in range(size))

    if sum(sum_of_rows) != sum(sum_of_cols):
        return False

    if sum_of_rows[0] != diag1:
        return False

    if sum_of_rows[0] != diag2:
        return False

    return True


