def magic_square_test(matrix):
    # calculate the sum of the first row
    magic_constant = sum(matrix[0])
    # check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    # check columns
    for i in range(len(matrix)):
        if sum(row[i] for row in matrix) != magic_constant:
            return False
    # check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False
    return True

print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))

"""
The function works by first calculating the magic constant, which is the sum of the elements in the first row. Then, it checks all rows and columns to see if their sum equals the magic constant. Finally, it checks the sum of the two diagonals to see if they equal the magic constant. If all these checks pass, the function returns True, indicating that the matrix is a magic square. If any of the checks fail, the function returns False.
"""

# The following is an alternate solution that checks if the matrix is a square before running the checks.

def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    magic_constant = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    for i in range(len(matrix)):
        if sum(row[i] for row in matrix) != magic_constant:
            return False
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-