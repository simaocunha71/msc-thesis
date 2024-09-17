def remove_dirty_chars(str1: str, str2: str) -> str:
  dirty_chars = set(str2)
  return ''.join([char for char in str1 if char not in dirty_chars])