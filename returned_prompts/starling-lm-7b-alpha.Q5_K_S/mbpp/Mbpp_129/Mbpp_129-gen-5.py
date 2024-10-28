
def magic_square_test(matrix: list):
    n = len(matrix)
    col_sum = [0] * n
    row_sum = 0
    for i in range(n):
        row_sum += sum(matrix[i])
    for i in range(n):
        for j in range(n):
            row_sum += matrix[i][j]
            col_sum[i] += matrix[j][i]
    return (row_sum == col_sum[0] and row_sum == sum(col_sum))


