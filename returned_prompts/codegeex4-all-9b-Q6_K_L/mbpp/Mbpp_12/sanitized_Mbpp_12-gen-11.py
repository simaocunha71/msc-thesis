def sort_matrix(matrix: list) -> list:
  matrix.sort(key=sum)
  return matrix