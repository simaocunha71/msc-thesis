
def sequential_search(arr, element):
  is_found = False
  index = -1
  for i in range(len(arr)):
    if arr[i] == element:
      is_found = True
      index = i
      break
  return is_found, index


