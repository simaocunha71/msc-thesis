def find_Index(n: int) -> int:
  if n == 1:
    return 1
  i = 2
  while True:
    triangular_number = i * (i + 1) // 2
    if len(str(triangular_number)) == n:
      return i
    i += 1