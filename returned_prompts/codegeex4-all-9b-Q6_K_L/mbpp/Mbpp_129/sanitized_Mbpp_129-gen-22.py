def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    target_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != target_sum:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False
    return True