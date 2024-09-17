def max_of_nth(matrix: list, n: int) -> int:
  return max(matrix[i][n] for i in range(len(matrix)))