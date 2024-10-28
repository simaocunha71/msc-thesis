
def max_subarray_product(arr: list) -> int:
  max_product = arr[0]
  current_product = arr[0]
  for i in range(1, len(arr)):
    current_product = max(arr[i], current_product * arr[i], current_product)
    max_product = max(max_product, current_product)
  return max_product


