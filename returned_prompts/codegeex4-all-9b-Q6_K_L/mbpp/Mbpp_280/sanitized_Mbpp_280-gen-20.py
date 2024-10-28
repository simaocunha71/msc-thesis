def sequential_search(nums: list, el: int) -> tuple:
  try:
    return (True, nums.index(el))
  except ValueError:
    return (False, -1)