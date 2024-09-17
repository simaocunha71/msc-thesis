
def magic_square_test(mat):
  if len(mat) == 0:
    return False

  # Get size of the magic square
  n = len(mat)

  # Get the sum of the first row to use as the magic sum
  magic_sum = sum(mat[0])

  # Check each row for a magic sum
  for row in mat:
    if sum(row) != magic_sum:
      return False

  # Check each column for a magic sum
  for col in range(n):
    if sum(mat[i][col] for i in range(n)) != magic_sum:
      return False

  # Check the diagonals for a magic sum
  if sum(mat[i][i] for i in range(n)) != magic_sum:
    return False
  if sum(mat[i][n - i - 1] for i in range(n)) != magic_sum:
    return False

  return True


