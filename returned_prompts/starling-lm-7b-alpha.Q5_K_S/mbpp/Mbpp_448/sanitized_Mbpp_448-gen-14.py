def cal_sum(n: int) -> int:
  perrin_nums = []
  for i in range(n+1):
    perrin_nums.append(i*(i+1)//2)
  return sum(perrin_nums)