
def magic_square_test(matrix):
  # get the size of the matrix
  n = len(matrix)
  # get the sum of the first row
  magic_constant = sum(matrix[0])
  # check rows, columns, and diagonals
  for i in range(n):
    if sum(matrix[i]) != magic_constant or sum([row[i] for row in matrix]) != magic_constant or sum(matrix[i][i] for i in range(n)) != magic_constant or sum(matrix[i][n-i-1] for i in range(n)) != magic_constant:
      return False
  return True


