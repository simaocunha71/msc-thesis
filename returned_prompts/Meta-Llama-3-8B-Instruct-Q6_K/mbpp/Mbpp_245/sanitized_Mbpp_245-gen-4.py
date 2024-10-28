def max_sum(arr):
  n = len(arr)
  incl = [0] * n
  excl = [0] * n

  excl[0] = 0
  for i in range(1, n):
    excl[i] = max(incl[i-1], excl[i-1])

  incl[0] = arr[0]
  for i in range(1, n):
    incl[i] = max(incl[i-1]+arr[i], excl[i-1])

  return max(incl[n-1], excl[n-1]) if n > 0 else 0