def is_Monotonic(nums: list) -> bool:
  increasing = decreasing = True
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      increasing = False
    if nums[i] < nums[i + 1]:
      decreasing = False
  return increasing or decreasing