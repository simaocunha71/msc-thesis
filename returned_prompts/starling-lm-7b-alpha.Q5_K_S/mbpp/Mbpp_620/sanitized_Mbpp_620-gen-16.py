def largest_subset(nums:list):
  nums.sort()
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return 1
  if nums[0] % nums[1] == 0:
    return largest_subset(nums[1:]) + 1
  return largest_subset(nums[1:])