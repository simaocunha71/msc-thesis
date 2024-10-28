def remove_dirty_chars(dirty_str: str, clean_str: str) -> str:
  return dirty_str.translate({ord(c): None for c in clean_str})

