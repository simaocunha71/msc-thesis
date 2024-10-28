def max_sum(arr):
  n = len(arr)
  if n < 3:
    return -1
  inc = [0]*n
  dec = [0]*n
  max_sum = [0]*n
  inc[0] = arr[0]
  dec[n-1] = arr[n-1]
  for i in range(1, n):
    inc[i] = max(inc[i-1], arr[i]) if inc[i-1] > arr[i] else arr[i]
  for i in range(n-2, -1, -1):
    dec[i] = max(dec[i+1], arr[i]) if dec[i+1] > arr[i] else arr[i]
  for i in range(1, n-1):
    max_sum[i] = inc[i] + dec[i] - arr[i]
  return max(max_sum)