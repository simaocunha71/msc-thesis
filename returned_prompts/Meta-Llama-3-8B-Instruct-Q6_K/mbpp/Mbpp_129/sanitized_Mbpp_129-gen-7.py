def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False

    total = sum(matrix[0])
    for row in matrix:
        if sum(row) != total:
            return False

    for col in range(len(matrix[0])):
        if sum([matrix[i][col] for i in range(len(matrix))]) != total:
            return False

    return True