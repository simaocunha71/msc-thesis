
def recursive_list_sum(my_list):
  if type(my_list) == list:
    return sum(map(recursive_list_sum, my_list))
  else:
    return my_list


