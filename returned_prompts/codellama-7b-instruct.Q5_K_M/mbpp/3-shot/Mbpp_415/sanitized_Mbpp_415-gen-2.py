def max_Product(arr: list) -> tuple:
  max_product = -1
  max_pair = (-1,-1)
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      product = arr[i] * arr[j]
      if product > max_product:
        max_pair = (arr[i], arr[j])
        max_product = product
  return max_pair