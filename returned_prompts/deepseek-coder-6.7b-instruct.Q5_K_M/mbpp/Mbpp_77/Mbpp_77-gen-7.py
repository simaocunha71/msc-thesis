
def is_Diff(num):
  num_str = str(num)
  len_num = len(num_str)
  sum1 = 0
  sum2 = 0
  for i in range(len_num):
    if i % 2 == 0:
      sum1 += int(num_str[i])
    else:
      sum2 += int(num_st[i])
  return abs(sum1 - sum2) % 11 == 0


