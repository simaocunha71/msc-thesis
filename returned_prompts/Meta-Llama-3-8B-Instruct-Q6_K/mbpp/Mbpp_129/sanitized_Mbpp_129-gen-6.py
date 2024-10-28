def magic_square_test(matrix):
  if len(matrix) != len(matrix[0]):
    return False
  sum_row = sum(matrix[0])
  for row in matrix:
    if sum(row) != sum_row:
      return False
  for col in range(len(matrix[0])):
    sum_col = sum([row[col] for row in matrix])
    if sum_col != sum_row:
      return False
  sum_diag1 = sum([matrix[i][i] for i in range(len(matrix))])
  sum_diag2 = sum([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])
  if sum_diag1 != sum_row or sum_diag2 != sum_row:
    return False
  return True