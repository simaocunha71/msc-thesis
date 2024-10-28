def cal_sum(n: int) -> int:
  perrin = [0, 2, 3]
  for i in range(3, n):
    perrin.append(perrin[i-1] + perrin[i-2])
  return sum(perrin)