def magic_square_test(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False