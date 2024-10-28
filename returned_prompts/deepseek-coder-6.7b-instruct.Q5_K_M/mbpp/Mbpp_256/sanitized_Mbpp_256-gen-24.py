def count_Primes_nums(n):
  prime = [True for i in range(n+1)]
  p = 2
  while (p * p <= n):
    if (prime[p] == True):
      for i in range(p * p, n+1, p):
        prime[i] = False
    p += 1
  count = 0
  for i in range(2, n):
    if prime[i]:
      count += 1
  return count