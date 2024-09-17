def max_sum_list(nums:list)->list:
  max_sum_list = []
  for num in nums:
    if sum(num) > sum(max_sum_list):
      max_sum_list = num
  return max_sum_list