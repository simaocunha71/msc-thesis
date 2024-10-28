def sequential_search(nums: list, element: int) -> tuple:
  if element in nums:
    return (True, nums.index(element))
  else:
    return (False, -1)