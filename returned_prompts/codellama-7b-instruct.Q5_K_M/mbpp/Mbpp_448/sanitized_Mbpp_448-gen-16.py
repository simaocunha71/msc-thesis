def cal_sum(n: int) -> int:
  """
  Perrin numbers are numbers that have the digits of the numbers in a given range.
  For example, the 4-digit number 2582 has the digits 2, 5, 8, and 2.
  """
  start, end = 10, 10**n
  res = 0
  for i in range(start, end):
    num = i
    while num > 0:
      res += num % 10
      num //= 10
  return res