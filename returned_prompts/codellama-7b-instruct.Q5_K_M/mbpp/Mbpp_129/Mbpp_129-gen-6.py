"""
def magic_square(matrix):
    # Initialize a list to store the sum of each row, column, and diagonal
    sums = [0, 0]

    # Calculate the sums of each row and column
    for i in range(4):
        for j in range(4):
            sums[0] += matrix[i][j]
            sums[1] += matrix[j][i]

    # Check if the sums of the rows and columns are equal
    if sums[0] != sums[1]:
        return False

    # Calculate the sum of the diagonals
    sums[0] = 0
    for i in range(4):
        sums[0] += matrix[i][i]
        sums[1] -= matrix[i][3-i]

    # Check if the sum of the diagonals is equal to the sum of the rows and columns
    if sums[0] != sums[1]:
        return False

    # Check if all the numbers in the matrix are unique
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i != k and j != k and matrix[i][j] == matrix[k][k]:
                    return False

    return True
"""
