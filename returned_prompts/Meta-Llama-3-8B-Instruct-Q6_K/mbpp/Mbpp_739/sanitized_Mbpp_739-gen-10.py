def find_Index(n):
  i = 1
  count = 0
  while True:
    tri_num = i*(i+1)//2
    count += len(str(tri_num))
    if count == n:
      return i
    i += 1