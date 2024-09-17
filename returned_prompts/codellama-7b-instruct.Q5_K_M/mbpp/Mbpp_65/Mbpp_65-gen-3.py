
def recursive_list_sum(my_list):
  if isinstance(my_list, list):
    return sum(map(recursive_list_sum, my_list))
  return my_list


