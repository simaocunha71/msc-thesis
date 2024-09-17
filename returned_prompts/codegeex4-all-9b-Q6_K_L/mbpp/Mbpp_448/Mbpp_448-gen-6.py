def cal_sum(n: int) -> int:
  a, b, c = 0, 1, 2
  sum_perrin = 0
  for _ in range(n):
    sum_perrin += c
    a, b, c = b, c, a + b + c
  return sum_perrin