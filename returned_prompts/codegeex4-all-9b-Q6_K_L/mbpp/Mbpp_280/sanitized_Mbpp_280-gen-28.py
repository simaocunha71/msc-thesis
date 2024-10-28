def sequential_search(arr: list, element: int) -> tuple:
  if element in arr:
    return True, arr.index(element)
  else:
    return False, -1