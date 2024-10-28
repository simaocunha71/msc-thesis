def max_of_nth(matrix: list, n: int) -> int:
  max_val = 0
  for row in matrix:
    if row[n] > max_val:
      max_val = row[n]
  return max_val