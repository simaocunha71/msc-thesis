def max_subarray_product(arr: list) -> int:
  n = len(arr)
  max_product = float('-inf')
  for i in range(n):
    product = 1
    for j in range(i, n):
      product *= arr[j]
      max_product = max(max_product, product)
  return max_product

