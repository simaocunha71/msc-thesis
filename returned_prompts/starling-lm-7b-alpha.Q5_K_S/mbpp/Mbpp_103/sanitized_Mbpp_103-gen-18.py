def eulerian_num(n: int, m: int) -> int:
  if m == 0:
    return 0
  if m == 1:
    return 1
  if m > 1:
    return (n + m) * (eulerian_num(n, m - 1) + 1)