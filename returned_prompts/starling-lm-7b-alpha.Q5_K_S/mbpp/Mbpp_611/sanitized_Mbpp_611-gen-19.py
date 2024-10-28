def max_of_nth(matrix: list, n: int) -> int:
  return max([row[n-1] for row in matrix])