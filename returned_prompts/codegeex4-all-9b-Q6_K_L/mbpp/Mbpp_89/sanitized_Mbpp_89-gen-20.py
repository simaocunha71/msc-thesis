def closest_num(n):
  if n >= 1 and n <= 9:
    return n - 1
  elif n >= 10 and n <= 99:
    return n - 10
  elif n >= 100 and n <= 999:
    return n - 100
  elif n >= 1000 and n <= 9999:
    return n - 1000
  elif n >= 10000 and n <= 99999:
    return n - 10000
  else:
    return "Number is too large"