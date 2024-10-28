def remove_dirty_chars(s1: str,s2: str) -> str:
  for c in s2:
    s1 = s1.replace(c, "")
  return s1