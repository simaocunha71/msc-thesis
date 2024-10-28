def last_Digit_Factorial(n):
  fact = 1
  for i in range(1, n + 1):
    fact = (fact * i)
  while fact % 10 == 0:
    fact //= 10
  return fact % 10