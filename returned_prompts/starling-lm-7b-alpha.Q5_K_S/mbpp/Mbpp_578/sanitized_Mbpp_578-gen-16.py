def interleave_lists(*args):
  flattened_list = []
  for arg in args:
    flattened_list.extend(arg)
  return flattened_list