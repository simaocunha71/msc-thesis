def max_sum(arr):
  arr.sort()
  max_sum = 0
  decreasing_sum = 0
  for i in range(len(arr)-1, -1, -1):
    decreasing_sum += arr[i]
    if decreasing_sum > max_sum:
      max_sum = decreasing_sum
    if arr[i] < arr[i-1]:
      decreasing_sum = 0
  return max_sum