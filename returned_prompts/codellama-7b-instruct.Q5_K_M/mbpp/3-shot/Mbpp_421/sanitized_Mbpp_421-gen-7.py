def concatenate_tuple(my_tuple: tuple, delimiter: str) -> str:
  return delimiter.join(str(item) for item in my_tuple)