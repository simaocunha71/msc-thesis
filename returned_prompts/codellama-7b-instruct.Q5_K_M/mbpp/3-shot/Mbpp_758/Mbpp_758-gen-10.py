
def unique_sublists(my_list):
  my_dict = {}
  for sublist in my_list:
    tup = tuple(sublist)
    if tup in my_dict:
      my_dict[tup] += 1
    else:
      my_dict[tup] = 1
  return my_dict


