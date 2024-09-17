
def last_Digit_Factorial(n):
  fact = 1
  for i in range(1,n+1):
    fact = (fact * i) % 10
  return fact


