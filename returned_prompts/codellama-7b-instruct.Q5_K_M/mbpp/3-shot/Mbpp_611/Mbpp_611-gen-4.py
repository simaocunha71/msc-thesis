
def max_of_nth(matrix: list, n: int) -> int:
  return max(col for col in zip(*matrix))


