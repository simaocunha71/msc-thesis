def max_Product(arr):
  n = len(arr)
  if n == 0:
    return (0, 0)
  max_so_far = max_ending_here = arr[0]
  for i in range(1, n):
    max_ending_here = max(arr[i], max_ending_here * arr[i],
                                  max_so_far * arr[i])
    max_so_far = max(max_so_far, max_ending_here)
  return (max_so_far, max_ending_here)