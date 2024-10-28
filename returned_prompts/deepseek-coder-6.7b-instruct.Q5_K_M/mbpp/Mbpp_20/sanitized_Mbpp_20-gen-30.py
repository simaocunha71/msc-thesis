def is_woodall(n):
  num_str = str(n)
  digits = list(map(int, str(n)))
  product = 1
  for digit in digits:
    product *= digit
  return product == int(num_str)