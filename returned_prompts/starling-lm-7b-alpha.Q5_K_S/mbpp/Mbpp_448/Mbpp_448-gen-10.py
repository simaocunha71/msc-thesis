
def cal_sum(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1:
    return 2
  return cal_sum(n-1) + cal_sum(n-2) + n


