def max_product(arr):
  max_product = 1
  for i in range(len(arr)):
    max_product = max(max_product, arr[i])
    for j in range(i+1, len(arr)):
      max_product = max(max_product, arr[i] * arr[j])
  return max_product