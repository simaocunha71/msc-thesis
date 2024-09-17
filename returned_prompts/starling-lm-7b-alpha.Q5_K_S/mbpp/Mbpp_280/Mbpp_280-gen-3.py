
def sequential_search(nums: list, target: int) -> tuple:
  for i in range(len(nums)):
    if nums[i] == target:
      return (True, i)
  return (False, -1)


