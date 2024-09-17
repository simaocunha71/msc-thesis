
def remove_dirty_chars(dirty_str: str, clean_str: str) -> str:
  clean_str_set = set(clean_str)
  dirty_str_list = list(dirty_str)
  for char in dirty_str_list:
    if char in clean_str_set:
      dirty_str_list.remove(char)
  return "".join(dirty_str_list)


