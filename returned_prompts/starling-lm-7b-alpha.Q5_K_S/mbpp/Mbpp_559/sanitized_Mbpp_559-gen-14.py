def max_sub_array_sum(nums: list,limit: int) -> int:
  curr_sum = max_sum = curr_start = max_start = float('-inf')
  for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum > max_sum:
      max_sum = curr_sum
      max_start = curr_start
    if curr_sum < 0:
      curr_sum = 0
      curr_start = i + 1
  if limit > max_sum:
    limit = max_sum
  return sum(nums[max_start : max_start + limit])