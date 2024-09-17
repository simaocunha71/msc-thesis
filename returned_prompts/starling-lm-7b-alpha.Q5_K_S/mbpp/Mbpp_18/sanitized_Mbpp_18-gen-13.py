def remove_dirty_chars(s1: str, s2: str) -> str:
  return ''.join(c for c in s1 if c not in s2)