
def find_star_num(n: int) -> int:
  if n == 0:
    return 0
  return n + find_star_num(n-1)


