def cal_sum(n):
  perrin_nums = [0, 2, 3]
  for i in range(3, n):
    perrin_nums.append(perrin_nums[i-1] + perrin_nums[i-2])
  return sum(perrin_nums)