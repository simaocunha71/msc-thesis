def max_Abs_Diff(my_list):
  return max(abs(i-j) for i,j in zip(my_list,my_list[1:]))