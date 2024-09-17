def max_sum_list(nums: list) -> list:
  max_list = nums[0]
  for i in nums:
    if sum(i) > sum(max_list):
      max_list = i
  return max_list