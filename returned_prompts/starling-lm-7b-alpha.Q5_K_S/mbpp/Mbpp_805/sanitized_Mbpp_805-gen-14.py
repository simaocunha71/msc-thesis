def max_sum_list(list_of_list):
  max_sum = 0
  max_sum_list = []
  for sublist in list_of_list:
    if sum(sublist) > max_sum:
      max_sum = sum(sublist)
      max_sum_list = sublist
  return max_sum_list