def find_Index(n):
  index = 0
  while True:
    index += 1
    triangular = index*(index+1)//2
    if len(str(triangular)) == n:
      return index

