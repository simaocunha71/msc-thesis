
def max_sum_list(lst):
  max_sum = 0
  max_list = []
  for sub_list in lst:
    if sum(sub_list) > max_sum:
      max_sum = sum(sub_list)
      max_list = sub_list
  return max_list


