def magic_square_test(matrix):
  sum_rows = [sum(row) for row in matrix]
  sum_cols = [sum(col) for col in zip(*matrix)]
  diag1 = sum(matrix[i][i] for i in range(len(matrix)))
  diag2 = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))
  if sum_rows == sum_cols == diag1 == diag2:
    return True
  else:
    return False