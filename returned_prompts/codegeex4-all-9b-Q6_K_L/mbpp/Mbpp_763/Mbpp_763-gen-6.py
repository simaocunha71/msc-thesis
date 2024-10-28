def find_min_diff(arr,n):
  if n < 2:
    return 0
  arr.sort()
  min_diff = arr[1] - arr[0]
  for i in range(1, n-1):
    min_diff = min(min_diff, arr[i+1] - arr[i])
  return min_diff

