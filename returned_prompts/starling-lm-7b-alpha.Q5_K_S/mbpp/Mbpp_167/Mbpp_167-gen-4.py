
def next_power_of_2(n):
  if n == 0:
    return 1
  else:
    return 2 ** (len(bin(n)) - 3)


