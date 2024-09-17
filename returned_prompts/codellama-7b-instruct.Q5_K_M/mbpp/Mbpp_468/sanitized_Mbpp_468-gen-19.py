def max_product(arr: list) -> int:
  arr_len = len(arr)
  if arr_len == 1:
    return arr[0]
  if arr_len == 2:
    return arr[0] * arr[1]
  if arr_len == 3:
    return max(arr[0] * arr[1] * arr[2], arr[0] * arr[2] * arr[1], arr[1] * arr[2] * arr[0])

  max_product = arr[0] * arr[1] * arr[2]
  max_product_list = [arr[0], arr[1], arr[2]]
  for i in range(3, arr_len):
    max_product = max(max_product, arr[i] * arr[i-1] * arr[i-2], arr[i] * max_product_list[1] * max_product_list[2], arr[i-1] * arr[i-2] * max_product_list[2])
    max_product_list = [arr[i], arr[i-1], arr[i-2]]
  return max_product