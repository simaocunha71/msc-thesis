def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    for col in range(n):
        if sum([row[col] for row in matrix]) != expected_sum:
            return False
    return True