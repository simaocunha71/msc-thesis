def cal_sum(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  perrin_nums = [0, 1, 2]
  for i in range(3, n+1):
    perrin_nums.append(perrin_nums[i-1] + perrin_nums[i-2] + 2*perrin_nums[i-3])
  return sum(perrin_nums)