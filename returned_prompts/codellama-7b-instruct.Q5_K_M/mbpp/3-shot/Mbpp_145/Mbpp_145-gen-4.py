
def max_Abs_Diff(my_list: list) -> int:
  return max(abs(my_list[i]-my_list[i+1]) for i in range(len(my_list)-1))


