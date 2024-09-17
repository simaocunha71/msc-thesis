def magic_square_test(matrix):
  sum_rows = [sum(row) for row in matrix]
  sum_cols = [sum(row[j] for row in matrix) for j in range(len(matrix[0]))]
  if sum(sum_rows) != sum(sum_cols):
    return False
  sqrt_size = int(len(matrix) ** 0.5)
  if len(matrix) != len(matrix[0]) or len(matrix) % 2 == 1:
    return False
  if sum(sum_rows) % 2 != 0:
    return False
  if sum_rows.count(sum_rows[0]) != sqrt_size:
    return False
  if sum_cols.count(sum_cols[0]) != sqrt_size:
    return False
  return True