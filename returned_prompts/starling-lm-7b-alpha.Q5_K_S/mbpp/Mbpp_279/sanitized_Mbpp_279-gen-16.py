def is_num_decagonal(n):
  if n == 0:
    return 0
  elif n == 1:
    return 10
  else:
    return n * (10 + 9 * (n-1))