
def is_majority(arr, n, element):
  count = 0
  for i in range(n):
    if arr[i] == element:
      count += 1
    if count > n // 2:
      return True
  return False


