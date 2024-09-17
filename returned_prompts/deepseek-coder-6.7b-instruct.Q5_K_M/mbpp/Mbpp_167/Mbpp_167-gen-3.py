
def next_power_of_2(n):
  if (n and not(n & (n - 1))):
    return n
  while (n):
    n = n >> 1
  return 1 << (n + 1)


