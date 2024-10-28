def max_sum_list(list_of_lists: list) -> list:
  max_list = list_of_lists[0]
  for i in list_of_lists:
    if sum(i) > sum(max_list):
      max_list = i
  return max_list