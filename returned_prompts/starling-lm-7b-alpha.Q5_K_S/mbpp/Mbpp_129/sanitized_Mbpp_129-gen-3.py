def magic_square_test(matrix):
    # Check if all rows have the same sum
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False

    # Check if all columns have the same sum
    column_sums = [sum(col) for col in zip(*matrix)]
    if len(set(column_sums)) != 1:
        return False

    # Check if the diagonal sum is equal to the row/column sum
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    if diagonal_sum != row_sums[0]:
        return False

    # Check if the anti-diagonal sum is equal to the row/column sum
    anti_diagonal_sum = sum(matrix[i][-1-i] for i in range(len(matrix)))
    if anti_diagonal_sum != row_sums[0]:
        return False

    return True