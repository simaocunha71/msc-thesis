def max_subarray_product(arr):
  max_val = arr[0]
  for i in range(1, len(arr)):
    max_val = max(max_val, max_val * arr[i], arr[i])
  return max_val