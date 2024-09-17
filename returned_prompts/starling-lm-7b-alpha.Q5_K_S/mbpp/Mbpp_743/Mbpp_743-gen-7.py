
def rotate_right(nums: list, n: int) -> list:
  nums.insert(0,nums.pop(n))
  return nums


