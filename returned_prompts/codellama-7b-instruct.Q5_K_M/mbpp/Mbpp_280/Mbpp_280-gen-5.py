
def sequential_search(arr, element):
  index = -1
  found = False
  for i in range(len(arr)):
    if arr[i] == element:
      index = i
      found = True
      break
  return found, index


