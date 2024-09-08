def magic_square_test(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    if sum(matrix[i][n-i-1] for i in range(n)) != target_sum:
        return False

    return True