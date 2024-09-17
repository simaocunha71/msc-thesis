
def max_sub_array_sum_repeated(arr, k, n):
  max_sum = 0
  for i in range(k):
    max_sum = max(max_sum, sum(arr))
    arr = [x + y for x, y in zip(arr, arr)]
  return max_sum


