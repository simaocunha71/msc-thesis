def max_difference(tup_list:list)->int:
  max_diff = 0
  for i in range(len(tup_list)):
    for j in range(i+1,len(tup_list)):
      max_diff = max(max_diff,tup_list[j][0]-tup_list[i][1])
  return max_diff