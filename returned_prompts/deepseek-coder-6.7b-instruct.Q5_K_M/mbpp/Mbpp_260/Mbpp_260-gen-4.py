
def newman_prime(n):
  prime_count = 0
  num = 2
  while True:
    if is_prime(num):
      prime_count += 1
      if prime_count == n:
        return num
    num += 1

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

