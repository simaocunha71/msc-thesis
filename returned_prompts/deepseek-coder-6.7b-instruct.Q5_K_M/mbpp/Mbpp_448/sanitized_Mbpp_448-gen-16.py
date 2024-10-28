def perrin(n):
  p = [3, 0, 2]
  for i in range(3, n+1):
    p.append(p[i-1] + p[i-2])
  return p[n]
def cal_sum(n):
  return perrin(n)