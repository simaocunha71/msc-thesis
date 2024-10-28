def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    expected_sum = n * (n**2 + 1) // 2
    for i in range(n):
        if sum(matrix[i]) != expected_sum:
            return False
        row_sum = sum(matrix[i])
        if row_sum != expected_sum:
            return False
    return True