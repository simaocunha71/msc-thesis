
def rotate_right(nums: list, d: int) -> list:
  return nums[d:] + nums[:d]


