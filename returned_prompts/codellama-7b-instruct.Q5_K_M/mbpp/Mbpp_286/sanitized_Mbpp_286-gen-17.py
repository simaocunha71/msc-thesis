def max_sub_array_sum_repeated(arr, k, n):
  curr_sum = 0
  max_sum = -1
  for i in range(n):
    curr_sum = 0
    for j in range(i, n + i, n):
      curr_sum += arr[j % n]
      if curr_sum > max_sum:
        max_sum = curr_sum

  return max_sum * k