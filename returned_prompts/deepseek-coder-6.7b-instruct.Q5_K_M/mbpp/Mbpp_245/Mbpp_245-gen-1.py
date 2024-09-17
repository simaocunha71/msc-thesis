
def max_sum(arr):
  n = len(arr)
  if n < 3:
    return -1
  inc = [0]*n
  dec = [0]*n
  msis = [0]*n
  max_sum = 0
  inc[0] = arr[0]
  dec[n-1] = arr[n-1]
  for i in range(1, n):
    inc[i] = arr[i] if inc[i-1] > arr[i] else inc[i-1]
  for i in range(n-2, -1, -1):
    dec[i] = arr[i] if dec[i+1] > arr[i] else dec[i+1]
  for i in range(0, n):
    msis[i] = inc[i] + dec[i] - arr[i]
  for i in range(0, n):
    if max_sum < msis[i]:
      max_sum = msis[i]
  return max_sum


