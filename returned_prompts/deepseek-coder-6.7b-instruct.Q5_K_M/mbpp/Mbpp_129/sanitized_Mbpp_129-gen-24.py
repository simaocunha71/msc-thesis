def magic_square_test(matrix):
  # Find the sum of the first row
  magic_constant = sum(matrix[0])
  # Check each row for a match
  for row in matrix:
    if sum(row) != magic_constant:
      return False
  # Check each column for a match
  for i in range(len(matrix)):
    if sum(row[i] for row in matrix) != magic_constant:
      return False
  # Check the diagonals for a match
  if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
    return False
  if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
    return False
  # If all tests pass, return True
  return True