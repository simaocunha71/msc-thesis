
def prime_num(num):
  if num == 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

