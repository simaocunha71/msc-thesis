def magic_square_test(matrix):
    # get the size of the square
    size = len(matrix)

    # calculate the magic constant
    magic_constant = size * (size * size + 1) // 2

    # calculate the row sums
    row_sums = [sum(row) for row in matrix]
    if any(sum != magic_constant for sum in row_sums):
        return False

    # calculate the column sums
    column_sums = [sum(row[i] for row in matrix) for i in range(size)]
    if any(sum != magic_constant for sum in column_sums):
        return False

    # calculate the diagonal sums
    diagonal_sums = [sum(matrix[i][i] for i in range(size)), sum(matrix[i][size - i - 1] for i in range(size))]
    if any(sum != magic_constant for sum in diagonal_sums):
        return False

    return True