def cal_sum(n):
  perrin_nums = [3, 0, 2]
  for i in range(3, n+1):
    perrin_nums.append(perrin_nums[i-2] + perrin_nums[i-3])
  return sum(perrin_nums[:n])