
def max_sub_array_sum(arr: list, k: int) -> int:
  max_sum = float("-inf")
  current_sum = 0
  for i in range(len(arr)):
    current_sum = max(current_sum + arr[i], arr[i])
    if i >= k - 1:
      max_sum = max(max_sum, current_sum)
      current_sum -= arr[i - k + 1]
  return max_sum


