def max_of_nth(matrix, n):
  max_val = None
  for row in matrix:
    if n < len(row):
      if max_val is None or row[n] > max_val:
        max_val = row[n]
  return max_val