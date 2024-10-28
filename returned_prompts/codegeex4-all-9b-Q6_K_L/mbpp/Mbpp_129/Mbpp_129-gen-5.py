def magic_square_test(matrix: list) -> bool:
  sum_row = sum(matrix[0])
  sum_column = sum(matrix[0])
  for row in matrix:
    if sum_row != sum(row):
      return False
  for col in range(len(matrix[0])):
    if sum_column != sum(matrix[row][col] for row in range(len(matrix))):
      return False
  return True

