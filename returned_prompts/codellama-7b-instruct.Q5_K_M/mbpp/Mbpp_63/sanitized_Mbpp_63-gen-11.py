def max_difference(tup_list):
  max_diff = 0
  for i in range(len(tup_list)):
    for j in range(i, len(tup_list)):
      current_diff = abs(tup_list[j][0] - tup_list[i][0])
      if current_diff > max_diff:
        max_diff = current_diff
  return max_diff