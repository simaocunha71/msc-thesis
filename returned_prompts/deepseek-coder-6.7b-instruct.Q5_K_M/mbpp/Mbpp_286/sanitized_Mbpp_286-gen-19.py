def max_sub_array_sum_repeated(arr: list, k: int, m: int) -> int:
  total_sum = 0
  n = len(arr)
  for i in range(k):
    total_sum += sum(arr)
  max_sum = float('-inf')
  for i in range(n * m):
    max_sum = max(max_sum, total_sum)
    total_sum = total_sum - arr[i % n] + arr[(i + n) % n]
  return max_sum