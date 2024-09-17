
def eulerian_num(n: int, m: int) -> int:
  if n == 0 or m == 0:
    return 1
  else:
    return eulerian_num(n-1, m) + eulerian_num(n-1, m-1)


