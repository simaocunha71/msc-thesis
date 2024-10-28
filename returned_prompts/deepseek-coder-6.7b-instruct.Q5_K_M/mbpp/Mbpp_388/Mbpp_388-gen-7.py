
def highest_Power_of_2(n):
  return 1 << (n - 1).bit_length()


