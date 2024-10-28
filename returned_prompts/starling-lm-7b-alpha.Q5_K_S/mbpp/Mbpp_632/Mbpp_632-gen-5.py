
def move_zero(nums:list):
  zero_index = nums.index(0)
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[zero_index] = nums[i]
      nums[i] = 0
      zero_index += 1
  return nums


