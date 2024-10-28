def max_sub_array_sum(arr: list,k: int) -> int:
  max_sum = 0
  current_sum = 0
  for i in range(len(arr)):
    current_sum = max(current_sum + arr[i], arr[i])
    if current_sum > max_sum:
      max_sum = current_sum
    if current_sum < 0:
      current_sum = 0
  return max_sum