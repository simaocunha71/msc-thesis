def newman_prime(n):
  count = 0
  num = 2
  while count < n:
    num += 1
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
      count += 1
  return num