def diff_even_odd(nums: list):
  return nums[0] - nums[1] if nums[0] % 2 == 0 else nums[1] - nums[0]