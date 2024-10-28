
def find_Index(n: int) -> int:
  i = 1
  while True:
    tn = (i * (i + 1)) // 2
    if len(str(tn)) == n:
      return i
    i += 1


