def magic_square_test(matrix):
  sum_r = sum(matrix[0])
  sum_c = sum(sum(row) for row in matrix)
  sum_d1 = sum(matrix[0][0] + matrix[1][1] + matrix[2][2])
  sum_d2 = sum(matrix[0][2] + matrix[1][1] + matrix[2][0])
  if sum_r == sum_c and sum_d1 == sum_r and sum_d2 == sum_r:
    return True
  return False