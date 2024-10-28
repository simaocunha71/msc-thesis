
def count_Primes_nums(n: int) -> int:
  count = 0
  for i in range(2, n):
      if is_not_prime(i) == False:
          count += 1
  return count


