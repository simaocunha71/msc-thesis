
def magic_square_test(matrix: list):
  matrix_len = len(matrix)
  for i in range(matrix_len):
    if sum(matrix[i]) != sum(matrix[0]):
      return False
  for i in range(matrix_len):
    if sum([matrix[j][i] for j in range(matrix_len)]) != sum(matrix[0]):
      return False
  for i in range(matrix_len):
    if sum([matrix[j][i] for j in range(matrix_len)]) != sum(matrix[i]):
      return False
  return True


