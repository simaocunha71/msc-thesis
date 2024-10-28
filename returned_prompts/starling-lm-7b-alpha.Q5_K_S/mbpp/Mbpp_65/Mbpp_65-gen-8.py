
def recursive_list_sum(input_list):
  total = 0
  for item in input_list:
    if isinstance(item, list):
      total += recursive_list_sum(item)
    else:
      total += item
  return total


