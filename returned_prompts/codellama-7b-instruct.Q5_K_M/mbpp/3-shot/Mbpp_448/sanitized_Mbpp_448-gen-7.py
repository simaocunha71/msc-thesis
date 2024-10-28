def cal_sum(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return cal_sum(n-1) + cal_sum(n-2)