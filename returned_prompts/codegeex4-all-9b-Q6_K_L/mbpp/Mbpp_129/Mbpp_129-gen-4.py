def magic_square_test(matrix):
  magic_sum = sum(matrix[0])
  for row in matrix:
    if sum(row) != magic_sum:
      return False
  for col in range(len(matrix)):
    if sum(matrix[row][col] for row in range(len(matrix))) != magic_sum:
      return False
  return True

