
def is_majority(arr, n, elem):
  count = 0
  for i in range(n):
    if arr[i] == elem:
      count += 1
      if count > n/2:
        return True
  return False


