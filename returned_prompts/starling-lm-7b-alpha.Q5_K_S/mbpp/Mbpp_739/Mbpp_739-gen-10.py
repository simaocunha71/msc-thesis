
def find_Index(n):
  for i in range(1, 1000000):
    if len(str(i*(i+1)//2)) == n:
      return i
  return -1


