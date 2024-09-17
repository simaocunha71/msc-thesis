
def max_product(arr: list) -> int:
  n = len(arr)
  if n == 0:
    return 0
  if n == 1:
    return arr[0]
  if n == 2:
    return max(arr[0], arr[1])
  if n == 3:
    return max(arr[0] * arr[1] * arr[2], arr[0] * arr[2], arr[1] * arr[2])

  max_prod = arr[0] * arr[1] * arr[2]
  max_prod_arr = [arr[0], arr[1], arr[2]]

  for i in range(3, n):
    curr_max_prod = max(
        max_prod_arr[0] * arr[i],
        max_prod_arr[1] * arr[i],
        max_prod_arr[2] * arr[i],
        arr[i - 2] * arr[i - 1] * arr[i],
    )

    max_prod_arr[2] = max_prod_arr[1]
    max_prod_arr[1] = max_prod_arr[0]
    max_prod_arr[0] = curr_max_prod

  return max_prod


