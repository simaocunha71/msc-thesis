
def max_sub_array_sum_repeated(arr, k, n):
  total_sum = sum(arr)
  max_sum = float('-inf')
  current_sum = 0
  for i in range(k):
    for j in range(n):
      current_sum += arr[j]
      max_sum = max(current_sum, max_sum)
      if current_sum < 0:
        current_sum = 0
    arr = arr[1:] + arr[:1]
  return max_sum


