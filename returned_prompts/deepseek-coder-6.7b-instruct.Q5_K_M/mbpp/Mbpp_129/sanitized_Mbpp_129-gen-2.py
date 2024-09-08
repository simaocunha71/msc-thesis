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