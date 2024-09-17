def recursive_list_sum(my_list):
  total = 0
  for i in my_list:
    if isinstance(i, list):
      total += recursive_list_sum(i)
    else:
      total += i
  return total