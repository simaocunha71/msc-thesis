def count_Primes_nums(n):
  if n < 2:
    return 0
  for i in range(2, n):
    if is_prime(i):
      count += 1
  return count