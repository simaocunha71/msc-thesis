def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    total = sum(matrix[0])
    for row in matrix:
        if sum(row) != total:
            return False
    for col in zip(*matrix):
        if sum(col) != total:
            return False
    return True