def max_difference(tup_list):
  max_diff = 0
  for i in range(len(tup_list)):
    for j in range(i+1, len(tup_list)):
      diff = abs(tup_list[i][1] - tup_list[j][1])
      if diff > max_diff:
        max_diff = diff
  return max_diff