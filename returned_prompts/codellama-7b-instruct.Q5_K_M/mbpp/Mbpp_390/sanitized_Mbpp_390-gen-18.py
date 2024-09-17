def add_string(my_list: list, format_string: str) -> list:
  return [format_string.format(i) for i in my_list]