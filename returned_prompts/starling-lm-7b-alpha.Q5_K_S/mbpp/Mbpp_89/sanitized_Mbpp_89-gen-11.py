def closest_num(n: int) -> int:
  for i in range(n-1, 0, -1):
    if i >= 1:
      return i
  return 1