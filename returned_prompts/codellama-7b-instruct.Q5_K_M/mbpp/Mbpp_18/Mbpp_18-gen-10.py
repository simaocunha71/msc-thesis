
def remove_dirty_chars(str1: str, str2: str) -> str:
  dirty_chars = set(str2)
  clean_str = ''.join(c for c in str1 if c not in dirty_chars)
  return clean_str


