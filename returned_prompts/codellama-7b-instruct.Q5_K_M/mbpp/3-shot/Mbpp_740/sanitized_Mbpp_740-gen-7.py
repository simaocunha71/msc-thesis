def tuple_to_dict(my_tuple):
  dictionary = {}
  for i in range(0, len(my_tuple), 2):
    dictionary[my_tuple[i]] = my_tuple[i + 1]
  return dictionary