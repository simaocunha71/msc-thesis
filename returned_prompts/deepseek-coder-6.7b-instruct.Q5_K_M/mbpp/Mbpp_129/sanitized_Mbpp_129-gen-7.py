def magic_square_test(matrix):
    # Get size of matrix
    size = len(matrix)

    # Get sum of first row
    magic_constant = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False

    # Check columns
    for i in range(size):
        if sum(row[i] for row in matrix) != magic_constant:
            return False

    # Check diagonal
    if sum(matrix[i][i] for i in range(size)) != magic_constant:
        return False
    if sum(matrix[i][size - i - 1] for i in range(size)) != magic_constant:
        return False

    return True