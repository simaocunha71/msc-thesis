def count_integer(my_list: list) -> int:
  return len([x for x in my_list if isinstance(x, int)])