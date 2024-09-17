def find_star_num(n: int) -> int:
  if n < 1:
    return 0
  else:
    return find_star_num(n-1) + n

