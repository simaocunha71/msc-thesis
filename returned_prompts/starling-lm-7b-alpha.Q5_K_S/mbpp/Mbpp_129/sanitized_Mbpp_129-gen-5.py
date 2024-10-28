def magic_square_test(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]) or not all(len(row) == n for row in matrix):
        return False
    row_sum = sum(matrix[i][i] for i in range(n))
    col_sum = sum(matrix[i][i%n] for i in range(n))
    diag1 = sum(matrix[i][i] for i in range(n))
    diag2 = sum(matrix[i][n-1-i] for i in range(n))
    return (row_sum == col_sum == diag1 == diag2) and all(sum(row) == row_sum for row in matrix) and \
        all(sum(col) == col_sum for col in zip(*matrix))