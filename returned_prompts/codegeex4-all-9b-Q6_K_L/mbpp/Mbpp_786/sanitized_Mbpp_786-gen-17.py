def right_insertion(nums: list, target: int) -> int:
  return bisect.bisect_right(nums, target)