def move_zero(nums: list):
  nums.sort(key = lambda x: (x == 0, x))
  return nums

