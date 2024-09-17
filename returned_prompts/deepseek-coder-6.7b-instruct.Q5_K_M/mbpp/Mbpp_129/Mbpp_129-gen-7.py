
def magic_square_test(matrix):
    # convert matrix to 1D list
    flatten_matrix = [i for sublist in matrix for i in sublist]

    # get the sum of the first row
    magic_constant = sum(matrix[0])

    # check rows and columns
    for i in range(len(matrix)):
        if sum(matrix[i]) != magic_constant or sum([row[i] for row in matrix]) != magic_constant:
            return False

    # check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant or sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False

    return True


