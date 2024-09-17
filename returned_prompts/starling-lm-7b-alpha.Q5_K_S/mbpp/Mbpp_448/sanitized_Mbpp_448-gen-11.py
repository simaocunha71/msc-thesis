def cal_sum(n: int) -> int:
  perrin_nums = []
  for i in range(1,n+1):
    perrin_nums.append(i*(i+1)//2)
  sum_perrin_nums = sum(perrin_nums)
  return sum_perrin_nums