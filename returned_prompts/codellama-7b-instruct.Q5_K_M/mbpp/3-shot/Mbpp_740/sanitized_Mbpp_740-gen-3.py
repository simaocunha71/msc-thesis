def tuple_to_dict(my_tuple):
  my_dict = {}
  for i in range(0, len(my_tuple), 2):
    my_dict[my_tuple[i]] = my_tuple[i + 1]
  return my_dict