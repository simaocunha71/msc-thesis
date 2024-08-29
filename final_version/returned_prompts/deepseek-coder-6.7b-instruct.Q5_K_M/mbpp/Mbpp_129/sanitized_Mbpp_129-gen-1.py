def magic_square_test(matrix):
    # Get the size of the matrix
    size = len(matrix)

    # Initialize the sums for the rows, columns and diagonals
    row_sums = [0]*size
    col_sums = [0]*size
    diag_sum1 = 0
    diag_sum2 = 0

    # Calculate the sums
    for i in range(size):
        for j in range(size):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
            if i == j:
                diag_sum1 += matrix[i][j]
            if i + j == size - 1:
                diag_sum2 += matrix[i][j]

    # Check if all sums are the same
    if len(set(row_sums)) == 1 and len(set(col_sums)) == 1 and diag_sum1 == diag_sum2 == row_sums[0] == col_sums[0]:
        return True
    else:
        return False