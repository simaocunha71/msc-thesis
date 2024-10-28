def newman_prime(n):
  prime_nums = [2, 3, 5, 7]
  while len(prime_nums) < n:
    temp_num = (prime_nums[-1] ** 2) + 1
    while temp_num % prime_nums[0] != 0:
      temp_num += 1
    if is_prime(temp_num):
      prime_nums.append(temp_num)
  return prime_nums[n-1]
def is_prime(n):
  if n == 2 or n == 3 or n == 5:
    return True
  elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
  else:
    root_n = int(n ** 0.5)
    for i in range(7, root_n + 1, 6):
      if n % i == 0 or n % (i + 2) == 0:
        return False
    return True