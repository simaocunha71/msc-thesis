def add_pairwise(nums: tuple) -> tuple:
  return tuple(map(sum, zip(nums[:-1], nums[1:])))