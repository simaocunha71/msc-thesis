
def sequential_search(arr: list, element: int) -> tuple:
  for index, value in enumerate(arr):
    if value == element:
      return True, index
  return False, -1

