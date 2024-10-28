
def highest_Power_of_2(n):
  if n <= 0:
    return 0
  i = 0
  while n > (1 << i):
    i += 1
  return (1 << (i - 1))


