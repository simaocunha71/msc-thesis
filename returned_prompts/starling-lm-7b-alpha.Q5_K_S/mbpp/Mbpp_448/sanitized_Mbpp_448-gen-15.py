def cal_sum(n):
  perrin_nums = [0] * (n+1)
  perrin_nums[0] = 0
  perrin_nums[1] = 1
  for i in range(2, n+1):
    perrin_nums[i] = i + sum(perrin_nums[1:i])
  return sum(perrin_nums)