def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    for i in range(len(matrix)):
        if sum(matrix[i]) != sum(matrix[0]):
            return False
    return True