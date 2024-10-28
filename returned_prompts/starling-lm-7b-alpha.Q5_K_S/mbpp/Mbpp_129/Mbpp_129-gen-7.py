
def magic_square_test(matrix: list):
  magic_num = sum(matrix[0])
  for i in range(1, 4):
    if sum(matrix[i]) != magic_num:
      return False
  for i in range(4):
    if sum(matrix[i][0:4]) != magic_num:
      return False
    if sum(matrix[0:4][i]) != magic_num:
      return False
  return True


