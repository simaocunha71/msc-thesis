
def left_insertion(nums: list, target: int) -> int:
  for i, num in enumerate(nums):
    if num > target:
      return i
  return len(nums)


