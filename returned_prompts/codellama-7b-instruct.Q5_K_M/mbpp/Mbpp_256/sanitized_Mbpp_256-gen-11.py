def count_Primes_nums(n: int) -> int:
  count = 0
  for i in range(2, n):
    if is_prime(i):
      count += 1
  return count
def is_prime(n: int) -> bool:
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True