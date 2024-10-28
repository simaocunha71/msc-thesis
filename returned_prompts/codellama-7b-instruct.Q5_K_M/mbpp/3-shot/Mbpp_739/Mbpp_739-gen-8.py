
def find_Index(n: int) -> int:
  for i in range(n*1000000000, 1000000000):
    if i % 10 == 0:
      continue
    if (i % 10 - 1)**2 + (i // 10)**2 == i:
      return i


