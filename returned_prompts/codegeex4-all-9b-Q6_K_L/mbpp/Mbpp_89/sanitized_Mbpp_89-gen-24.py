def closest_num(n: int) -> int:
  for i in range(n-1, 0, -1):
    if n % i == 0:
      return i
  return 0