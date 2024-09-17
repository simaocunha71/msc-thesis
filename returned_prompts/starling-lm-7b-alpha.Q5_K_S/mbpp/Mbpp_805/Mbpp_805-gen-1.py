
def max_sum_list(nums: list) -> list:
  max_sum = 0
  for sublist in nums:
    current_sum = sum(sublist)
    if current_sum > max_sum:
      max_sum = current_sum
      max_sublist = sublist
  return max_sublist


