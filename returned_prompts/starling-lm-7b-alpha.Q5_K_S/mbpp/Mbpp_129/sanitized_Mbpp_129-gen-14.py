def magic_square_test(matrix):
  col_sum = sum(matrix[0])
  row_sum = matrix[0][0]
  magic_sum = col_sum
  for i in range(1, len(matrix)):
    row_sum += matrix[i][0]
    col_sum += matrix[0][i]
    magic_sum += matrix[i][i]
  for i in range(len(matrix)):
    if sum(matrix[i]) != col_sum or sum(col_sum) != row_sum:
      return False
  return magic_sum == row_sum and magic_sum == col_sum