def cal_sum(n):
  a = 0
  for i in range(1,n+1):
    a += i * 2 ** (i - 1)
  return a