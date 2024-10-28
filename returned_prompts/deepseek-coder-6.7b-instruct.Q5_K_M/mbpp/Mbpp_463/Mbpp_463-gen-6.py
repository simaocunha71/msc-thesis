
def max_subarray_product(arr):
  n = len(arr)
  max_end_here = 1
  min_end_here = 1
  max_so_far = 1
  for i in range(n):
    if arr[i] > 0:
      max_end_here = max_end_here * arr[i]
      min_end_here = min(min_end_here * arr[i], 1)
    elif arr[i] < 0:
      temp = max_end_here
      max_end_here = max(min_end_here * arr[i], 1)
      min_end_here = temp * arr[i]
    else:
      max_end_here = 0
      min_end_here = 1
    max_so_far = max(max_so_far, max_end_here)
  return max_so_far


