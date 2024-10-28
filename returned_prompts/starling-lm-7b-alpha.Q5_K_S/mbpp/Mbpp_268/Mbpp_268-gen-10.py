
def find_star_num(n: int) -> int:
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return 2*find_star_num(n-1) + 1


