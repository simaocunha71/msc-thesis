def last_Digit_Factorial(n: int) -> int:
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return last_Digit_Factorial(n-1) * n % 10