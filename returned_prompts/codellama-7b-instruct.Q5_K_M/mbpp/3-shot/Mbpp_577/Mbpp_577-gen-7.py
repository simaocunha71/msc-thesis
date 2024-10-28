
def last_Digit_Factorial(n):
  if n < 0:
    return -1
  if n <= 1:
    return n
  while n % 10 == 0:
    n /= 10
  return n % 10


