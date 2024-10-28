def sort_matrix(matrix):
  sorted_matrix = sorted(matrix, key=sum, reverse=True)
  return sorted_matrix