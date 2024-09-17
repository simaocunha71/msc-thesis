def search(nums: list) -> int:
  if len(nums) == 1:
    return nums[0]
  if len(nums) == 2:
    if nums[0] == nums[1]:
      return None
    else:
      return nums[0]
  if nums[0] == nums[1]:
    return search(nums[2:])
  if nums[-2] == nums[-1]:
    return search(nums[:-2])
  return nums[0]