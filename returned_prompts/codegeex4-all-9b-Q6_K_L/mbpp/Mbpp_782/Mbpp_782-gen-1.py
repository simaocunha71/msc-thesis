def odd_length_sum(arr):
  sum = 0
  for i in range(len(arr)):
    if i % 2 == 0:
      sum += sum(arr[i:])
  return sum

