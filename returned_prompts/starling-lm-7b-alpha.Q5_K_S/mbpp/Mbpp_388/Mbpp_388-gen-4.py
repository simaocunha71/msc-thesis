
def highest_Power_of_2(n):
  if n == 0:
    return 0
  else:
    return 2 ** (len(bin(n)) - 3)


