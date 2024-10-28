def recursive_list_sum(lst: list)-> int:
  sum_lst = 0
  for i in lst:
    if isinstance(i, list):
      sum_lst += recursive_list_sum(i)
    else:
      sum_lst += i
  return sum_lst