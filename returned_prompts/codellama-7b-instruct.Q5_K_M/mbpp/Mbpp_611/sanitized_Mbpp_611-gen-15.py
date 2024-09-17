def max_of_nth(matrix: list, column: int) -> int:
  return max(map(lambda x: x[column], matrix))