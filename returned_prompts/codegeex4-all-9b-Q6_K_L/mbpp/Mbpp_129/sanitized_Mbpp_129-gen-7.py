def magic_square_test(matrix):
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Calculate the sum of the first row
    target_sum = sum(matrix[0])

    # Check each row
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check each column
    for col in range(len(matrix)):
        if sum(matrix[row][col] for row in range(len(matrix))) != target_sum:
            return False

    # Check the two diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != target_sum:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != target_sum:
        return False

    # If all checks pass, it's a magic square
    return True