def find_star_num(n):
  if n == 1:
    return 1
  else:
    return find_star_num(n-1) + n