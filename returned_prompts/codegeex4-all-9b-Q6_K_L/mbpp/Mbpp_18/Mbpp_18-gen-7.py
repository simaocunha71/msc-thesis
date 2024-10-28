def remove_dirty_chars(dirty_str: str, clean_str: str) -> str:
  return ''.join([char for char in dirty_str if char not in clean_str])


