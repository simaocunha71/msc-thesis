def sequential_search(array: list, element: int) -> tuple:
  for i, num in enumerate(array):
    if num == element:
      return True, i
  return False, -1

