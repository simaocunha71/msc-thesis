def newman_prime(n: int) -> int:
  def newman_shanks_williams_prime(n: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n < len(primes):
      return primes[n]
    p = primes[-1]
    k = 0
    while True:
      k += 1
      p = 2 * p + 1
      for prime in primes:
        if p % prime == 0:
          break
      else:
        primes.append(p)
        if len(primes) == n:
          return p
  return newman_shanks_williams_prime(n)