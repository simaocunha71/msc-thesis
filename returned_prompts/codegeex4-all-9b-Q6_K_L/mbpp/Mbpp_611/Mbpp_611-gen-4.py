def max_of_nth(matrix: list, n: int) -> int:
  max_num = max(row[n] for row in matrix)
  return max_num

