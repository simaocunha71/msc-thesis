def tuple_to_dict(my_tuple):
  keys = my_tuple[::2]
  values = my_tuple[1::2]
  return dict(zip(keys, values))