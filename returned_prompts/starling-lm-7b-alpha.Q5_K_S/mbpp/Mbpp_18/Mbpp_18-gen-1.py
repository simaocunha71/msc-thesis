
def remove_dirty_chars(s: str, dirty_chars: str) -> str:
  for c in dirty_chars:
    s = s.replace(c, '')
  return s


