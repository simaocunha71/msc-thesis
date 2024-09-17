def highest_Power_of_2(n: int) -> int:
  i = 1
  while i <= n:
    i *= 2
  return i // 2