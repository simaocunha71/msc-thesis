def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
  total_sum = sum(arr)
  max_so_far = max_ending_here = 0
  for i in range(k * n):
    max_ending_here = max_ending_here + arr[i % n]
    if max_ending_here < 0:
      max_ending_here = 0
    elif max_so_far < max_ending_here:
      max_so_far = max_ending_here
  return max_so_far