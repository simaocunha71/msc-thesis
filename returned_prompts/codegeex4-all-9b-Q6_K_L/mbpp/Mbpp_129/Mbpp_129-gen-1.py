def magic_square_test(matrix):
    n = len(matrix)
    # Check if the sum of each row is the same
    sum_row = sum(matrix[0])
    for row in matrix:
        if sum(row) != sum_row:
            return False

    # Check if the sum of each column is the same
    sum_col = sum(row[0] for row in matrix)
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != sum_col:
            return False

    # Check if the sum of the main diagonal is the same
    sum_diag = sum(matrix[i][i] for i in range(n))
    if sum_diag != sum_row:
        return False

    # Check if the sum of the secondary diagonal is the same
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    if sum_diag2 != sum_row:
        return False

    return True

