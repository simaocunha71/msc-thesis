def rotate_right(nums: list,n: int) -> list:
  return nums[-n:] + nums[:-n]