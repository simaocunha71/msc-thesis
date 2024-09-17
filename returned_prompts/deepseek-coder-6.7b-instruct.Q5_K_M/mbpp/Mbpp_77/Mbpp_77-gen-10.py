
def is_Diff(num):
  num = str(num)
  sum_diff = sum(int(num[i]) - int(num[i-1]) for i in range(1, len(num)))
  return sum_diff % 11 == 0


