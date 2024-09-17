def max_sum_list(list_of_lists: list) -> list:
  max_sum = 0
  max_list = []
  for lst in list_of_lists:
    sum_of_list = sum(lst)
    if sum_of_list > max_sum:
      max_sum = sum_of_list
      max_list = lst
  return max_list