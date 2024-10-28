def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
  max_sum = float('-inf')
  for _ in range(k):
    for i in range(n):
      if arr[i] > max_sum:
        max_sum = arr[i]
      curr_sum = arr[i]
      for j in range(i+1, n):
        curr_sum += arr[j]
        if curr_sum > max_sum:
          max_sum = curr_sum
  return max_sum