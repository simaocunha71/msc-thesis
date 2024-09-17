
def recursive_list_sum(nested_list: list)-> int:
  total = 0
  for item in nested_list:
    if isinstance(item, list):
      total += recursive_list_sum(item)
    else:
      total += item
  return total


