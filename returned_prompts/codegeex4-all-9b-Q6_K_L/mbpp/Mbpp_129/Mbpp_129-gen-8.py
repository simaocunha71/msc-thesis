def magic_square_test(magic_square):
    # Check if all rows sum to the same value
    row_sum = sum(magic_square[0])
    for row in magic_square[1:]:
        if sum(row) != row_sum:
            return False

    # Check if all columns sum to the same value
    for col in range(len(magic_square)):
        if sum(magic_square[row][col] for row in range(len(magic_square))) != row_sum:
            return False

    # Check if all diagonals sum to the same value
    if sum(magic_square[i][i] for i in range(len(magic_square))) != row_sum:
        return False
    if sum(magic_square[i][len(magic_square)-1-i] for i in range(len(magic_square))) != row_sum:
        return False

    return True