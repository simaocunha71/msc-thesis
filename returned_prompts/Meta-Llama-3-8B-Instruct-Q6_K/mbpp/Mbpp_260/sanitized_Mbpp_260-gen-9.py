def newman_prime(n: int) -> int:
  primes = []
  num = 7
  while len(primes) < n:
    if is_prime(num):
      primes.append(num)
    num += 2
  return primes[-1]
def is_prime(num: int) -> bool:
  if num < 2:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True