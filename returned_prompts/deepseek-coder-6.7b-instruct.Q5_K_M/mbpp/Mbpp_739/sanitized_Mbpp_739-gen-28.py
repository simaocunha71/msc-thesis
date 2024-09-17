def find_Index(n):
  i = 1
  while True:
    triangular = i*(i+1)//2
    if len(str(triangular)) == n:
      return i
    i += 1