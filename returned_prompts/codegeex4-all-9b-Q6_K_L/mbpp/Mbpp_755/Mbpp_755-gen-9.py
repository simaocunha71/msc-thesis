def second_smallest(nums: list) -> int:
  nums = sorted(set(nums))
  if len(nums) < 2:
    raise ValueError("List must contain at least two distinct elements")
  return nums[1]