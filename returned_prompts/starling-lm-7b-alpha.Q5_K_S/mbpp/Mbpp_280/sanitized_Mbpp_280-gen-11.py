def sequential_search(nums: list, target: int) -> tuple:
  for i, num in enumerate(nums):
    if target == num:
      return (True, i)
  return (False, -1)