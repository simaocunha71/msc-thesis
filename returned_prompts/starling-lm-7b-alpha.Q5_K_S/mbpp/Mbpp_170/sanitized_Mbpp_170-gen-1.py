def sum_range_list(nums, start_index, end_index):
  total = 0
  for i in range(start_index, end_index + 1):
    total += nums[i]
  return total