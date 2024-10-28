def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum != expected_sum:
            return False
    for i in range(n):
        col_sum = sum([matrix[j][i] for j in range(n)])
        if col_sum != expected_sum:
            return False
    diag1_sum = sum([matrix[i][i] for i in range(n)])
    diag2_sum = sum([matrix[i][n-i-1] for i in range(n)])
    if diag1_sum != expected_sum or diag2_sum != expected_sum:
        return False
    return True