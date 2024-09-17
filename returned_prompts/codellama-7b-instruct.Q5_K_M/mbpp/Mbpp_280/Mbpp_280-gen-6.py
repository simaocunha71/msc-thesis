
def sequential_search(arr: list, element: int) -> tuple:
  for i in range(len(arr)):
    if arr[i] == element:
      return (True, i)
  return (False, -1)


