
def magic_square_test(matrix: list) -> bool:
  row_sums = [sum(row) for row in matrix]
  col_sums = [sum(col) for col in zip(*matrix)]
  diag_sums = [sum(diagonal) for diagonal in zip(*matrix[i] for i in range(len(matrix)))]
  diag_sums.append(sum(reversed(diagonal) for diagonal in zip(*matrix[i] for i in range(len(matrix)))))

  return all(row_sums) == col_sums == diag_sums


