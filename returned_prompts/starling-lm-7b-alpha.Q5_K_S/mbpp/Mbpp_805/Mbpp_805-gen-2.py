
def max_sum_list(nums: list) -> list:
  max_sum = 0
  max_list = []
  for i in range(len(nums)):
    if sum(nums[i]) > max_sum:
      max_sum = sum(nums[i])
      max_list = nums[i]
  return max_list


