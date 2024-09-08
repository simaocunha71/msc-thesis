"""
def magic_square_test(matrix):
    # calculate the sum of the first row
    magic_constant = sum(matrix[0])
    # check each row
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    # check each column
    for col in range(len(matrix)):
        if sum(row[col] for row in matrix) != magic_constant:
            return False
    # check the diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False
    return True

print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16,, 3, 10, 5], [9, 6, 15, 4]]))
"""

