def magic_square_test(matrix):
    n = len(matrix)
    # Sum of elements in each row
    row_sums = [sum(row) for row in matrix]
    # Sum of elements in each column
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    # Sum of elements in the main diagonal
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    # Sum of elements in the secondary diagonal
    secondary_diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    # Check if all sums are equal
    return all(row_sum == col_sum == main_diag_sum == secondary_diag_sum for row_sum, col_sum in zip(row_sums, col_sums))