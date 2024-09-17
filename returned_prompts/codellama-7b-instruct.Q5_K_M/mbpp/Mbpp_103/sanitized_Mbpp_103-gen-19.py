def eulerian_num(n: int, m: int) -> int:
  def recur(n: int, m: int) -> int:
    if n == 0 or m == 0:
      return 1
    return recur(n-1, m) + recur(n-1, m-1)
  return recur(n, m)