def add_pairwise(nums):
  return tuple(x + y for x, y in zip(nums, nums[1:]))