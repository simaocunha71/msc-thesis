def newman_prime(n):
  if n == 1:
    return 2
  elif n == 2:
    return 3
  else:
    is_prime = False
    m = 1
    while not is_prime:
      m += 1
      is_prime = True
      for i in range(2, int(m ** 0.5)):
        if m % i == 0:
          is_prime = False
          break
    return m + newman_prime(n - 1)