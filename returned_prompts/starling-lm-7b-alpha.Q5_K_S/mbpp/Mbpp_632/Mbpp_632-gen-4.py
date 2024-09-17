
def move_zero(nums):
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[-1] = nums[-1], nums[i]
  return nums


