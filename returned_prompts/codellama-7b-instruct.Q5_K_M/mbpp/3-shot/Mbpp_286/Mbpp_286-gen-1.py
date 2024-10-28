
def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
  curr_sum = 0
  max_sum = 0
  for i in range(n):
      curr_sum += arr[i]
      if i < k:
          max_sum += arr[i]
      else:
          max_sum = max(max_sum, curr_sum - arr[i-k])
          curr_sum -= arr[i-k]
  return max_sum


