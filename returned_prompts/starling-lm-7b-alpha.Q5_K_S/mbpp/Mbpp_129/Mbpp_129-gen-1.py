
def magic_square_test(matrix: list) -> bool:
  magic_sum = sum(matrix[0])
  if magic_sum % 2 != 0:
    return False
  for row in matrix:
    if sum(row) != magic_sum:
      return False
  magic_sums = []
  for i in range(4):
    magic_sums.append(sum(matrix[j][i] for j in range(4)))
    if magic_sums[-1] != magic_sum:
      return False
  magic_sums = []
  for i in range(4):
    magic_sums.append(sum(matrix[i][j] for j in range(4)))
    if magic_sums[-1] != magic_sum:
      return False
  return True


