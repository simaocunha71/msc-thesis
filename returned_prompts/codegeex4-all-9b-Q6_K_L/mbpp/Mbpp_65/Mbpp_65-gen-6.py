def recursive_list_sum(nums):
  total_sum = 0
  for num in nums:
    if isinstance(num, list):
      total_sum += recursive_list_sum(num)
    else:
      total_sum += num
  return total_sum

