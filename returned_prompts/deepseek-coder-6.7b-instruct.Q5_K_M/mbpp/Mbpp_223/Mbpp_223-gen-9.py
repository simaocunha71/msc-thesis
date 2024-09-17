
def is_majority(arr, n, x):
  i =0 
  while i<n:
    if arr[i] == x:
      break
    i += 1
  if i == n:
    return False
  if ((n // x) <= i) and (arr[i + n // x] == x):
    return True
  return False


