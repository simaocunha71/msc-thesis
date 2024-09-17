def second_smallest(nums: list) -> int:
  nums.sort()
  return nums[1] if len(nums) > 1 else None

