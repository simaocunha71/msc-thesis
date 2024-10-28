def last(nums: list, target: int) -> int:
  return len(nums)-1-list(reversed(sorted(nums))).index(target)