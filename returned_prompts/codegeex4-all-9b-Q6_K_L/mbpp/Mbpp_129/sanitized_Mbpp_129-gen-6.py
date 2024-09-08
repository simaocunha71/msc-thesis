def magic_square_test(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Check if each row sums to the same value
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False

    # Check if each column sums to the same value
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    if len(set(col_sums)) != 1:
        return False

    # Check if the main diagonal sums to the same value
    main_diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
    if main_diag_sum != row_sums[0]:
        return False

    # Check if the secondary diagonal sums to the same value
    secondary_diag_sum = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))
    if secondary_diag_sum != row_sums[0]:
        return False

    return True