
def eulerian_num(n, m):
  if n == 0:
    return 0
  elif m == 0 or m == n:
    return 1
  else:
    return eulerian_num(n - 1, m - 1) + m * eulerian_num(n - 1, m)


