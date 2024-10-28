
def is_Diff(n):
  sum_digits = sum([int(i) for i in str(n)])
  return sum_digits % 11 == 0


