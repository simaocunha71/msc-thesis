def cal_sum(n: int) -> int:
  perrin_nums = [1, 1, 0, 0, 1, 1, 0, 1, 1, 1]
  perrin_sum = sum(perrin_nums[:n+1])
  return perrin_sum