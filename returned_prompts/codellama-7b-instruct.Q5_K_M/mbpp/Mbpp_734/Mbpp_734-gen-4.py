
def sum_Of_Subarray_Prod(arr: list) -> int:
  n = len(arr)
  if n == 1:
    return arr[0]
  if n == 2:
    return arr[0] * arr[1]

  total = 0
  for i in range(0, n):
    for j in range(i, n):
      prod = 1
      for k in range(i, j+1):
        prod = prod * arr[k]
      total += prod
  return total


