def remove_dirty_chars(dirty_str: str, clean_str: str) -> str:
  for char in clean_str:
    dirty_str = dirty_str.replace(char, "")
  return dirty_str

