def magic_square_test(matrix: list) -> bool:
  n = len(matrix)
  magic_sum = sum(matrix[0])
  for row in matrix:
    if sum(row) != magic_sum:
      return False
  for col in range(n):
    if sum(matrix[row][col] for row in range(n)) != magic_sum:
      return False
  for diag in range(n):
    if sum(matrix[diag][diag]) != magic_sum:
      return False
  if sum(matrix[diag][n - 1 - diag]) != magic_sum:
    return False
  return True