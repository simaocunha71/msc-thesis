def count_binary_seq(n):
  count = [0] * (2*n + 1)
  count[0] = 1
  for i in range(1, 2*n + 1):
    count[i] = 2 * count[i-1]
    if i >= n:
      count[i] += 1
  return count[2*n]