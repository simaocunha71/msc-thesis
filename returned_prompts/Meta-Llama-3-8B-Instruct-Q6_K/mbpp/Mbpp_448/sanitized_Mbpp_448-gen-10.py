def cal_sum(n):
  if n < 1:
    return 0
  a, b, c = 3, 2, 1
  total = 3
  for _ in range(2, n):
    a, b, c = b, c, a + b
    total += c
  return total