def remove_dirty_chars(s, dirty):
  return ''.join([c for c in s if c not in dirty])