def magic_square_test(matrix):
    n = len(matrix)
    if n % 2 == 0:
        return False

    # Check if the sum of each row is equal to the sum of each column
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != col_sum:
            return False

    # Check if the sum of the main diagonal is equal to the sum of the secondary diagonal
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    secondary_diagonal_sum = sum(matrix[i][n-i-1] for i in range(n))
    if main_diagonal_sum != secondary_diagonal_sum:
        return False

    return True

