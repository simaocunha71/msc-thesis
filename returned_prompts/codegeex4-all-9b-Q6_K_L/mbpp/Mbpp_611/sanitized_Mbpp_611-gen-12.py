def max_of_nth(matrix: list, n: int) -> int:
  return max(col[n-1] for col in matrix)