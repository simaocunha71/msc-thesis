
def max_of_nth(matrix: list, n: int) -> int:
  max_col = []
  for i in range(len(matrix)):
    max_col.append(matrix[i][n-1])
  return max(max_col)


