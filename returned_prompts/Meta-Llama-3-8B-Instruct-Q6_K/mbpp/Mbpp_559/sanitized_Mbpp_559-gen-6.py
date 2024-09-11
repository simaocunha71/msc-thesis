def max_sub_array_sum(lst, n):
  max_sum = current_sum = sum(lst[:n])
  for i in range(n, len(lst)):
    current_sum = current_sum - lst[i-n] + lst[i]
    max_sum = max(max_sum, current_sum)
  return max_sum