def move_zero(nums: list) -> list:
  for i in range(len(nums)):
    if nums[i] == 0:
      nums.remove(nums[i])
      nums.append(0)
  return nums