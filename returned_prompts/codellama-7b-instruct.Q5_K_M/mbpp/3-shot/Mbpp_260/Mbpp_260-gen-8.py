
def newman_prime(n: int) -> int:
  if n == 1:
    return 2
  if n == 2:
    return 3
  if n == 3:
    return 11
  if n == 4:
    return 29
  if n == 5:
    return 127
  if n == 6:
    return 239
  if n == 7:
    return 2033
  if n == 8:
    return 14947
  if n == 9:
    return 901971

  prime = 1
  i = 2
  while i <= n:
    if n % i == 0:
      prime = 0
      break
    i += 1
  if prime:
    return n
  else:
    return newman_prime(n + 1)


