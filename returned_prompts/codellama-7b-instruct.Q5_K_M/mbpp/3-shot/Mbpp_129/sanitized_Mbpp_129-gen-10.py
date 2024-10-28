def magic_square_test(matrix):
  rows_sum = 0
  cols_sum = 0
  for row in matrix:
    rows_sum += sum(row)
  for col in zip(*matrix):
    cols_sum += sum(col)
  if rows_sum == cols_sum:
    diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
    diag_sum2 = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    if rows_sum == diag_sum and rows_sum == diag_sum2:
      return True
  return False