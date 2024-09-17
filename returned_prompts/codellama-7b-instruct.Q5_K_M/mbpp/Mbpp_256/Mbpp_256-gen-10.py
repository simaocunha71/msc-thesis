
def count_Primes_nums(nums):
  count = 0
  for i in range(2, nums):
    if is_not_prime(i):
      continue
    count += 1
  return count


