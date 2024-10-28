
def move_zero(nums: list) -> list:
  zero_index = nums.index(0)
  for i in range(zero_index, len(nums)):
    if nums[i] == 0:
      nums[i], nums[zero_index] = nums[zero_index], nums[i]
      zero_index += 1
  return nums


