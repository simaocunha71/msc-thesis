
def sort_matrix(matrix: list) -> list:
  row_sums = [sum(row) for row in matrix]
  row_sums_sort = sorted(row_sums)
  sorted_matrix = [[matrix[i][j] for i, _ in enumerate(row_sums_sort) if row_sums[i] == row_sums_sort[j]] for j in range(len(row_sums_sort))]
  return sorted_matrix


