def check_Consecutive(nums: list) -> bool:
  if len(nums) < 2:
    return True
  for i in range(len(nums) - 1):
    if nums[i] + 1 != nums[i + 1]:
      return False
  return True