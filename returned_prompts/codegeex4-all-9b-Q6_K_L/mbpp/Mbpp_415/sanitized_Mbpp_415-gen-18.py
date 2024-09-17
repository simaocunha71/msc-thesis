def max_Product(nums: list) -> tuple:
  nums.sort(reverse=True)
  return (nums[0], nums[1])