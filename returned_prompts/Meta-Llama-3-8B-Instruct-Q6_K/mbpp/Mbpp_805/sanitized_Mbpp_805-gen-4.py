def max_sum_list(list_of_lists):
  max_sum = max(sum(sublist) for sublist in list_of_lists)
  return [sublist for sublist in list_of_lists if sum(sublist) == max_sum]