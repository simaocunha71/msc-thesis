
def magic_square_test(matrix):
    # convert to 1D list
    flat_list = [item for sublist in matrix for item in sublist]
    # find sum of first row
    magic_constant = sum(flat_list[0:len(matrix[0])])
    # check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    # check columns
    for col in range(len(matrix[0])):
        if sum(matrix[i][col] for i in range(len(matrix))) != magic_constant:
            return False
    # check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False
    return True


