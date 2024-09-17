def magic_square_test(square: list) -> bool:
  row_sum = sum(square[0])
  for row in square:
    if sum(row) != row_sum:
      return False
  col_sum = sum([row[i] for row in square])
  if col_sum != row_sum:
    return False
  diag_sum = sum([square[i][i] for i in range(len(square))])
  if diag_sum != row_sum:
    return False
  return True

