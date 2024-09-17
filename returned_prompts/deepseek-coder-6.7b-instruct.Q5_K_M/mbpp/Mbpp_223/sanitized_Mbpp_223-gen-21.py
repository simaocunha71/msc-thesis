def is_majority(arr, n, x):
  i = 0
  while i < n:
    if arr[i] == x:
      break
    i += 1
  
  if i == n:
    return False
  
  j = i + 1
  while j < n:
    if arr[j] != x:
      return False
    j += 1
  
  return True