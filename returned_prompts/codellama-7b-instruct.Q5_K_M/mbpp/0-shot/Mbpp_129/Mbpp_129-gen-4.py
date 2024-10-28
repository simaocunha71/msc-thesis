def magic_square_test(matrix):
    row_sum = [sum(row) for row in matrix]
    col_sum = [sum(col) for col in zip(*matrix)]
    diag1 = sum(matrix[i][i] for i in range(len(matrix)))
    diag2 = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
    if sum(row_sum) != 3*sum(col_sum): return False
    if sum(row_sum) != sum(diag1, diag2): return False
    return True


