def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = n * (n**2 + 1) // 2
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != expected_sum or col_sum != expected_sum:
            return False
    diagonal1_sum = sum(matrix[i][i] for i in range(n))
    diagonal2_sum = sum(matrix[i][n - i - 1] for i in range(n))
    if diagonal1_sum != expected_sum or diagonal2_sum != expected_sum:
        return False
    return True