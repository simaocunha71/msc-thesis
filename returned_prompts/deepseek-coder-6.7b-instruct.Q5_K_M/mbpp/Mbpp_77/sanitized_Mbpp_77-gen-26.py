def is_Diff(num):
  str_num = str(num)
  sum_even = sum(int(str_num[i]) for i in range(0, len(str_num), 2))
  sum_odd = sum(int(str_num[i]) for i in range(1, len(str_num), 2))
  return abs(sum_even - sum_odd) % 11 == 0