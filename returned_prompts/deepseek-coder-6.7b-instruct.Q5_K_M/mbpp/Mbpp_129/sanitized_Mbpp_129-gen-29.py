def magic_square_test(matrix):
    # convert the list of lists into a list of numbers
    flat_list = [item for sublist in matrix for item in sublist]
    # calculate the sum of the first row
    magic_constant = sum(matrix[0])
    # calculate the sum of each row, column, and diagonal
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(column) for column in zip(*matrix)]
    diag_sums = [sum(matrix[i][i] for i in range(len(matrix))),
                 sum(matrix[i][-i-1] for i in range(len(matrix)))]
    # return whether all the sums are equal to the magic constant
    return all(sums == magic_constant for sums in row_sums + col_sums + diag_sums)