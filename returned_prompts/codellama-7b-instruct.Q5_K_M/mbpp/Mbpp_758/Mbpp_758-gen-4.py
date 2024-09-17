
def unique_sublists(my_list: list) -> dict:
  my_dict = {}
  for sublist in my_list:
    sublist_tuple = tuple(sublist)
    if sublist_tuple in my_dict:
      my_dict[sublist_tuple] += 1
    else:
      my_dict[sublist_tuple] = 1
  return my_dict


