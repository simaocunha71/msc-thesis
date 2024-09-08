def magic_square_test(matrix):
    # First we calculate the sum of the first row
    magic_constant = sum(matrix[0])
    # Then we check the rows, columns and diagonals
    for i in range(len(matrix)):
        # Check rows
        if sum(matrix[i]) != magic_constant:
            return False
        # Check columns
        if sum(matrix[j][i] for j in range(len(matrix))) != magic_constant:
            return False
    # Check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False
    return True

# Testing the function
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[16, 3], [5, 11], [9, 6]])==False
assert magic_square_test([[2, 7, 6, 8], [9, 5, 1, 3], [4, 3, 15, 2], [14, 10, 7, 12]])==False
"""

# Testing the function
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==