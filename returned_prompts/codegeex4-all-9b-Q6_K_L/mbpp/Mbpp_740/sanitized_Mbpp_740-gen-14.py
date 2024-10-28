def tuple_to_dict(tup):
  dict_ = dict(zip(tup[::2], tup[1::2]))
  return dict_