
def sort_matrix(matrix: list):
  matrix.sort(key = lambda x: sum(x))
  return matrix


