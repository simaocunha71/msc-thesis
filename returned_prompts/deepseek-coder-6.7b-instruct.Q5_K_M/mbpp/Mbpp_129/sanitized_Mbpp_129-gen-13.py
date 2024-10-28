def magic_square_test(matrix):
    # convert the matrix into a 1-D list
    flattened_matrix = [element for sublist in matrix for element in sublist]

    # calculate the sum of the first row
    magic_constant = sum(matrix[0])

    # check if all rows, columns, and diagonals sum to the magic constant
    return (all(sum(row) == magic_constant for row in matrix) and
            all(sum(column) == magic_constant for column in zip(*matrix)) and
            sum(matrix[i][i] for i in range(len(matrix))) == magic_constant and
            sum(matrix[i][-i - 1] for i in range(len(matrix))) == magic_constant)