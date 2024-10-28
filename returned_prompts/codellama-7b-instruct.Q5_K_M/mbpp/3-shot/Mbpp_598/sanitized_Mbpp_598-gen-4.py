def armstrong_number(n):
  digits = [int(i) for i in str(n)]
  return sum(digits ** 3) == n