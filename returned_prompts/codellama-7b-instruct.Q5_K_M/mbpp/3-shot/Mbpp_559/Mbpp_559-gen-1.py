
def max_sub_array_sum(arr: list, n: int) -> int:
  max_sum = float("-inf")
  current_sum = 0
  for i in range(n):
    current_sum = max(current_sum + arr[i], arr[i])
    if current_sum > max_sum:
      max_sum = current_sum
  return max_sum


