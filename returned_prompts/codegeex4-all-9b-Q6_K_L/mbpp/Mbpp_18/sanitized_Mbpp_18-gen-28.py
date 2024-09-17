def remove_dirty_chars(dirty_string: str, clean_string: str) -> str:
  for char in clean_string:
    dirty_string = dirty_string.replace(char, '')
  return dirty_string