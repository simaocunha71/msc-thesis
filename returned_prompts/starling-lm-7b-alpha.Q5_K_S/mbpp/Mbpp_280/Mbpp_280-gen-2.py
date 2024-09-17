
def sequential_search(nums: list, target: int) -> tuple:
  for i in range(len(nums)):
    if target == nums[i]:
      return (True, i)
  return (False, -1)


