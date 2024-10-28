def sum_Of_Subarray_Prod(arr: list) -> int:
  total_sum = 0
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      total_sum += prod(arr[i:j+1])
  return total_sum