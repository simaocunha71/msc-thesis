def max_length(nums: list) -> tuple:
  max_len = 0
  for i in range(len(nums)):
    if len(nums[i]) > max_len:
      max_len = len(nums[i])
  return max_len, nums[nums.index(nums[i])]