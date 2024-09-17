
def remove_dirty_chars(s1: str,s2: str) -> str:
  return ''.join([i for i in s1 if i not in s2])


