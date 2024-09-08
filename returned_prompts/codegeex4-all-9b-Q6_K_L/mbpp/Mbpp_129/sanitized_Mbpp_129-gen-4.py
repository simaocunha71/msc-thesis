def magic_square_test(matrix):
    n = len(matrix)
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    sum_row = [sum(row) for row in matrix]
    sum_col = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    return sum_diag1 == sum_diag2 == sum_row == sum_col