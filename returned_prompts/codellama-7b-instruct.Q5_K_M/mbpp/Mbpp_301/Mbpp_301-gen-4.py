
def dict_depth(my_dict):
  max_depth = 1
  for key, value in my_dict.items():
    if isinstance(value, dict):
      max_depth = max(max_depth, dict_depth(value) + 1)
  return max_depth


