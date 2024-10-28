
def last_Digit_Factorial(n: int) -> int:
  if n == 0:
    return 1
  elif n % 10 == 0:
    return 0
  else:
    return last_Digit_Factorial(n-1) % 10


