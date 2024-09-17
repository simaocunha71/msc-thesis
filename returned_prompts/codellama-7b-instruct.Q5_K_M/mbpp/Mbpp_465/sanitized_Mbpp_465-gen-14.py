def drop_empty(my_dict):
  return {key: value for key, value in my_dict.items() if value}