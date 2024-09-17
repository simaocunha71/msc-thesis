def find_Index(n):
  t = 0
  for i in range(1, 10000):
    t += i
    if len(str(t)) == n:
      return t
  return -1