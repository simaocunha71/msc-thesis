
def add_string(my_list: list, format_string: str) -> list:
  result = []
  for item in my_list:
    result.append(format_string.format(item))
  return result


