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

print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
"""

# 1.5. Write a Python program to reverse a string.

"""
