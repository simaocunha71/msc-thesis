def magic_square_test(matrix):
    # your code goes here
    sum_row = [sum(row) for row in matrix]
    sum_col = [sum(column) for column in zip(*matrix)]
    sum_diag1 = sum(matrix[i][i] for i in range(len(matrix)))
    sum_diag2 = sum(matrix[i][-i - 1] for i in range(len(matrix)))

    return len(set(sum_row)) == 1 and len(set(sum_col)) == 1 and len(set([sum_diag1, sum_diag2])) == 1