
def last(nums: list, target: int) -> int:
  return len(nums) - nums[::-1].index(target)


