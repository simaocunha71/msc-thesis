def magic_square_test(matrix):
    sum_row = sum([sum(row) for row in matrix])
    sum_col = sum([sum([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix[0]))])
    sum_diagonal1 = sum([matrix[i][i] for i in range(len(matrix))])
    sum_diagonal2 = sum([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])
    return sum_row == sum_col and sum_row == sum_diagonal1 and sum_row == sum_diagonal2