def eulerian_num(n: int, m: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return m
  return m * (n + 1) + eulerian_num(n - 1, m + 1)