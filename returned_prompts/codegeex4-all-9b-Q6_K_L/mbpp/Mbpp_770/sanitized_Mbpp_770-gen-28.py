def odd_num_sum(n):
  sum = 0
  for i in range(1, n+1):
    sum += (2*i - 1)**4
  return sum