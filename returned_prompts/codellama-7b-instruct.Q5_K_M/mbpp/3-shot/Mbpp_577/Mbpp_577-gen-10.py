
def last_Digit_Factorial(n):
  if n < 0:
    return -1
  if n == 0:
    return 1
  result = 1
  for i in range(1, n+1):
    result *= i
  return result % 10


