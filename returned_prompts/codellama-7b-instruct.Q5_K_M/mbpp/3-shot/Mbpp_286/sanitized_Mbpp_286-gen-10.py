def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
  result = 0
  for i in range(n):
    curr_sum = 0
    for j in range(k):
      curr_sum += arr[i]
    result = max(result, curr_sum)
  return result