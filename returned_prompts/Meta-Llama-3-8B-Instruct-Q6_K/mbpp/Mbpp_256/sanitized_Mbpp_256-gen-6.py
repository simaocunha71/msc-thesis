import math
def count_Primes_nums(n):
  primes = 0
  for i in range(2, n):
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      primes += 1
  return primes