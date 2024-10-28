def max_sum_list(lst):
  max_sum = max(sum(sublist) for sublist in lst)
  return [sublist for sublist in lst if sum(sublist) == max_sum][0]