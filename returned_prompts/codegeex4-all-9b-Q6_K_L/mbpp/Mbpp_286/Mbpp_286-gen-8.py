def max_sub_array_sum_repeated(arr, k, n):
  max_sum = -float('inf')
  for i in range(n):
    current_sum = 0
    for j in range(k):
      current_sum += arr[i]
    max_sum = max(max_sum, current_sum)
    arr.append(arr[i])
  return max_sum

