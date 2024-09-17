def first_Digit(n):
  if n < 0:
    n = -n
  while n >= 10:
    n /= 10
  return int(n)

