
def magic_square_test(matrix: list) -> bool:
  rows = len(matrix)
  cols = len(matrix[0])
  if rows != cols:
    return False
  if rows%2 == 0:
    return False

  # calculate the sum of all elements of the matrix
  sum_of_matrix = sum([sum(row) for row in matrix])

  # calculate the sum of the rows, cols and diagonals
  sum_of_rows = sum([sum(row) for row in matrix])
  sum_of_cols = sum([sum(col) for col in zip(*matrix)])
  sum_of_diags = sum([sum(matrix[i][i] for i in range(rows)),sum(matrix[i][rows-1-i] for i in range(rows))])

  # check if the sums are equal
  if sum_of_matrix != sum_of_rows or sum_of_matrix != sum_of_cols or sum_of_matrix != sum_of_diags:
    return False

  return True


