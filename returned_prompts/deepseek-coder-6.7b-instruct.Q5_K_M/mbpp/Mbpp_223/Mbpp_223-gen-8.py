
def is_majority(arr, n, x):
  i = 0
  while (i < n):
    if (arr[i] == x and arr[i + n // 2] == x):
      return True
    i += 1
  return False


