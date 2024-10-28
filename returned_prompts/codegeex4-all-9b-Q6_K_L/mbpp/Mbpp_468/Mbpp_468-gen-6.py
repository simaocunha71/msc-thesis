def max_product(arr: list) -> int:
  product = 1
  for i in range(len(arr)):
    if arr[i] > 1:
      product *= arr[i]
  return product

