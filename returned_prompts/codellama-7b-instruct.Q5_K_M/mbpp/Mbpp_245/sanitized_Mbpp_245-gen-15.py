def max_sum(arr):
  max_sum = 0
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if arr[i] > arr[j]:
        max_sum += arr[i]
      else:
        max_sum += arr[j]
  return max_sum