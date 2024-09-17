def move_zero(nums: list):
  zero_index = len(nums)-1
  for i in range(len(nums)-1, -1, -1):
    if nums[i] == 0:
      nums[i], nums[zero_index] = nums[zero_index], nums[i]
      zero_index -= 1
  return nums