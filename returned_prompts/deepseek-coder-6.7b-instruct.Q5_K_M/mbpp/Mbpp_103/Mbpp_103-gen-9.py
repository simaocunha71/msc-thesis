
def eulerian_num(n, m):
  if n == 0:
    return 1
  elif m == 0 or m > n:
    return 0
  else:
    return sum(eulerian_num(n - i, i) for i in range(1, m + 1))


