
def last_Digit_Factorial(n: int):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n+1):
      result = (result * i) % 10
    return result


