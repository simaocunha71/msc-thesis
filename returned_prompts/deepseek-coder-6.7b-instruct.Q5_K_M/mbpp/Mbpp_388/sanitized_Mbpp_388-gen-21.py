def highest_Power_of_2(n):
  i = 0
  while (1 << i) <= n:
    i += 1
  return 1 << (i-1)