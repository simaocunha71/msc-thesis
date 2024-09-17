
def dict_depth(dictionary:dict)->int:
  max_depth = 0
  for key, value in dictionary.items():
    if isinstance(value, dict):
      depth = dict_depth(value) + 1
      if depth > max_depth:
        max_depth = depth
  return max_depth + 1


