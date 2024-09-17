def count_Set_Bits(n):
  count = 0
  while n:
    count += 1
    n &= n - 1
  return count