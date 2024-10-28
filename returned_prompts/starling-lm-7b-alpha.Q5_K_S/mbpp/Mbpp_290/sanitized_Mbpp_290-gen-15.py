def max_length(list_of_lists: list) -> tuple:
  max_length_list = max(list_of_lists, key = len)
  return len(max_length_list), max_length_list