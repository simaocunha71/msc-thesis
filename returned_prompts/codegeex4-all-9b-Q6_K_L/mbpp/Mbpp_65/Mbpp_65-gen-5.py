def recursive_list_sum(lst):
  total_sum = 0
  for element in lst:
    if isinstance(element, list):
      total_sum += recursive_list_sum(element)
    else:
      total_sum += element
  return total_sum

