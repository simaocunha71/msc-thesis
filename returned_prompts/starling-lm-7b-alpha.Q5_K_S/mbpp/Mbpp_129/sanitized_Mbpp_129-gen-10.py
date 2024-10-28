def magic_square_test(matrix):
    if len(matrix) != 4:
        return False
    if len(matrix[0]) != 4:
        return False
    if all(len(row) != 4 for row in matrix):
        return False
    if any(len(row) != 4 for row in matrix):
        return False
    if all(len(col) != 4 for col in zip(*matrix)):
        return False
    if any(len(col) != 4 for col in zip(*matrix)):
        return False

    # Calculate the row sums
    row_sums = [sum(row) for row in matrix]
    # Calculate the column sums
    col_sums = [sum(col) for col in zip(*matrix)]
    # Calculate the diagonal sums
    diag_sums = [sum(matrix[i][i] for i in range(4)), sum(matrix[i][-1-i] for i in range(4))]

    # Check if all sums are equal
    if row_sums != col_sums != diag_sums:
        return False

    # Check if the matrix is symmetric
    if matrix != [row[::-1] for row in matrix]:
        return False

    return True