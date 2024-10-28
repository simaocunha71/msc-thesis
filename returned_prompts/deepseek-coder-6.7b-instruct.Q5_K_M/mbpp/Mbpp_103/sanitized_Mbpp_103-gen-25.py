def eulerian_num(n: int, m: int):
  if n == 0:
    return 1
  if m == 0:
    return 0
  return (m**n + sum([eulerian_num(n-1, m)*eulerian_num(n, i-1) for i in range(1, m+1)]))