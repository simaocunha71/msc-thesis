
def cal_sum(n):
  perrin = [3, 0, 2]
  for i in range(3, n + 1):
    perrin.append(perrin[i - 1] + perrin[i - 2])
  return sum(perrin[:n])


