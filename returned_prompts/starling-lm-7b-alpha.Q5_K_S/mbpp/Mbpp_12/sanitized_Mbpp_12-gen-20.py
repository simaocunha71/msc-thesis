def sort_matrix(matrix: list):
  sorted_matrix = sorted(matrix, key = sum, reverse = True)
  return sorted_matrix