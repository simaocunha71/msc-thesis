def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != expected_sum - sum(matrix[i]) + matrix[i][j]:
                return False
    return True