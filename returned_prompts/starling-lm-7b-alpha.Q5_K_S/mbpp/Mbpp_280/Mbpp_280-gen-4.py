
def sequential_search(arr:list,target:int) -> tuple:
  for i, n in enumerate(arr):
    if n == target:
      return (True, i)
  return (False, -1)


