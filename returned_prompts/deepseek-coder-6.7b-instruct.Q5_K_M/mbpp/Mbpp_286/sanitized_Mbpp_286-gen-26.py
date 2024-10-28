def max_sub_array_sum_repeated(arr: list, k: int, l: int) -> int:
  total_sum = 0
  max_sum = -99999999999
  n = len(arr)
  for i in range(k*l):
    total_sum += arr[i % n]
    if total_sum > max_sum:
      max_sum = total_size
    if total_sum < 0:
      total_sum = 0
  return max_sum