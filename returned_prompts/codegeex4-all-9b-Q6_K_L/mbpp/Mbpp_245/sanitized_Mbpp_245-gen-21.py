def max_sum(arr):
  n = len(arr)
  max_ending_here = max_ending_so_far = 0

  for i in range(n):
      max_ending_here = max(0, max_ending_here + arr[i])
      max_ending_so_far = max(max_ending_so_far, max_ending_here)

  return max_ending_so_far