
def tuple_to_dict(my_tuple):
  dict_ = {}
  for i in range(0, len(my_tuple), 2):
    dict_.update({my_tuple[i]: my_tuple[i + 1]})
  return dict_


