def add_pairwise(nums):
  return tuple(a+b for a, b in zip(nums, nums[1:]))