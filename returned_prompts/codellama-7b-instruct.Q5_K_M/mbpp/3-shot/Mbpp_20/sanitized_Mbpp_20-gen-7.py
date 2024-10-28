def is_woodall(n):
  digits = [int(digit) for digit in str(n)]
  return sum(digits) == sum(digits[::-1])