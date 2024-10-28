def add_pairwise(nums: tuple) -> tuple:
  return tuple(nums[i] + nums[i+1] for i in range(len(nums)-1))