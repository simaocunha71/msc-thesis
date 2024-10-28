def search(arr):
  if len(set(arr)) == 2:
    return arr[arr.index(min(arr))+1]
  elif len(set(arr)) == 3:
    return arr[arr.index(max(arr))+1]
  else:
    return None