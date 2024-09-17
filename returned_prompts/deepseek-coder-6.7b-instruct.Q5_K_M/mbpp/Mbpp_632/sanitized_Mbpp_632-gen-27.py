def move_zero(nums):
  nums.sort(key = lambda x: x == 0)
  return nums