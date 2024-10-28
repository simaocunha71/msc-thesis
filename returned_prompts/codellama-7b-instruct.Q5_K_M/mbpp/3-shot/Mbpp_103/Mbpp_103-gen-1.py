
def eulerian_num(n: int, m: int) -> int:
  if n == 0 or m == 0:
    return 0
  if n == 1 or m == 1:
    return 1
  return (eulerian_num(n-1, m) + eulerian_num(n, m-1)) % 1000000007


