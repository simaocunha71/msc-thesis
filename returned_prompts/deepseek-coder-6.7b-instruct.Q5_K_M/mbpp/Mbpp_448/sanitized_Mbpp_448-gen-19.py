def cal_sum(n):
  perrin = [0, 2]
  for i in range(2, n):
    perrin.append(perrin[-1] + perrin[-2])
  return sum(perrin[:n])