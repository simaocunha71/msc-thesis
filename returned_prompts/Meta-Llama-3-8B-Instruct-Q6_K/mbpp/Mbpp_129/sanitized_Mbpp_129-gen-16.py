def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    expected_sum = n * (n * n + 1) // 2
    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum != expected_sum:
            return False
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != expected_sum:
            return False
    diag_sum = sum(matrix[i][i] for i in range(n))
    if diag_sum != expected_sum:
        return False
    diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    if diag_sum != expected_sum:
        return False
    return True