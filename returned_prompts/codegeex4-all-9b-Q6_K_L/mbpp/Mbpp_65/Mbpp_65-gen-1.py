def recursive_list_sum(nums: list) -> int:
  total = 0
  for num in nums:
    if isinstance(num, list):
      total += recursive_list_sum(num)
    else:
      total += num
  return total

