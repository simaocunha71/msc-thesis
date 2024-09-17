def cal_sum(n):
  a, b = 0, 1
  sum = 0
  for _ in range(n):
    sum += a
    a, b = b, a + b
  return sum