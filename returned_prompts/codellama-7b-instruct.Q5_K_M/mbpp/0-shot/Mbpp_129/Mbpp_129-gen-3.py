def magic_square_test(matrix):
    # check the length of each row and column is the same
    if len(matrix) != len(matrix[0]):
        return False

    # check the sum of each row and column is the same
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    if set(row_sums) != set(col_sums):
        return False

    # check the sum of the matrix is a magic number
    magic_number = sum(row_sums)
    if sum(magic_number) != magic_number:
        return False

    return True
