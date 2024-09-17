
def move_zero(nums: list) -> list:
  zero_ind = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[zero_ind] = nums[zero_ind], nums[i]
      zero_ind += 1
  return nums


