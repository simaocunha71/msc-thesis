def next_power_of_2(n):
  if n < 1:
    return 1
  else:
    return 2 ** ((n - 1).bit_length() + 1)  # or 2 ** (n.bit_length() + 1) in Python 3.6 and above