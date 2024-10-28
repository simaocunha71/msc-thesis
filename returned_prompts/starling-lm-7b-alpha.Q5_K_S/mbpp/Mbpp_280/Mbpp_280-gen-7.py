
def sequential_search(nums:list, element: int) -> tuple:
  index = -1
  for i in range(len(nums)):
    if nums[i] == element:
      index = i
  return (index != -1, index)


