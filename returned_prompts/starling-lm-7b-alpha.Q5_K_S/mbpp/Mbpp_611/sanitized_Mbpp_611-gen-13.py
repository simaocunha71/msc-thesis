def max_of_nth(matrix: list, n: int) -> int:
  max_nums = [row[n] for row in matrix]
  return max(max_nums)