def sequential_search(arr, element):
  for idx, val in enumerate(arr):
    if val == element:
      return True, idx
  return False, -1