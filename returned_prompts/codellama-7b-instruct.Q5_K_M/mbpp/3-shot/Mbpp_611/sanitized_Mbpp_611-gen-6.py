def max_of_nth(matrix: list,n: int) -> int:
  return max(map(lambda x: x[n], matrix))