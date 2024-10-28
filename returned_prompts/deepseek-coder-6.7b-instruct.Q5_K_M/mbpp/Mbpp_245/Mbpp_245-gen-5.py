
def max_sum(arr):
  n = len(arr)

  # Initialize variables
  inc = [0]*n
  dec = [0]*n
  max_bitonic = 0

  # Initialize both arrays as 1
  for i in range(n):
    inc[i] = dec[i] = 1

  # Compute optimized maximum sum sequence
  for i in range(1, n):
    for j in range(i):
      if arr[i] > arr[j] and inc[i] < inc[j]+1:
        inc[i] = inc[j]+1

  for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
      if arr[i] > arr[j] and dec[i] < dec[j]+1:
        dec[i] = dec[j]+1

  # Compute maximum bitonic sum
  for i in range(n):
    max_bitonic = max(max_bitonic, inc[i]+dec[i]-1)

  return max_bitonic


