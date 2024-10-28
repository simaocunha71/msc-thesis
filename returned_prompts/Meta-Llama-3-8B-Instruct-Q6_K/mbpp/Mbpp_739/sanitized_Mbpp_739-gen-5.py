def find_Index(n):
  i = 1
  count = 0
  while True:
    triangular = (i * (i + 1)) // 2
    count += len(str(triangular))
    if count == n:
      return i
    i += 1