def newman_prime(n):
  def newman_step(x, p):
    return (x ** 2 + 1) % p
  def newman_test(p):
    x = 2
    while True:
      x = newman_step(x, p)
      if x < p:
        continue
      if not x & 1:
        return False
      if x == 1:
        return True
      x = newman_step(x, p)
    return True
  x = 1
  while True:
    if newman_test(x):
      break
    x += 1
  i = 1
  while True:
    if newman_test(x + i * x):
      break
    i += 1
  return x + i * x