def last_Digit_Factorial(n):
  factorial = 1
  for i in range(1,n+1):
    factorial = (factorial * i) % 10
  return factorial