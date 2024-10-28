def sequential_search(arr, ele):
  found = False
  index = -1
  for i in range(len(arr)):
    if arr[i] == ele:
      found = True
      index = i
      break
  return found, index