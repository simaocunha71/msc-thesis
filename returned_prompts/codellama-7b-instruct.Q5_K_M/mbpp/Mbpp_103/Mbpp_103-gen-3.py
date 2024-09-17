
def eulerian_num(n: int, m: int) -> int:
  if n == m == 1:
    return 1
  if n == 1 or m == 1:
    return 1
  return eulerian_num(n-1, m-1) + eulerian_num(n-1, m)


