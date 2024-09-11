def multiple_to_single(lst):
  return int("".join(map(str, lst)))  # convert each integer to string, join them together and convert back to integer