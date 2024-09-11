def max_sum_list(lists):
  max_sum = max(sum(lst) for lst in lists)
  return [lst for lst in lists if sum(lst) == max_sum]  # return the list with the highest sum