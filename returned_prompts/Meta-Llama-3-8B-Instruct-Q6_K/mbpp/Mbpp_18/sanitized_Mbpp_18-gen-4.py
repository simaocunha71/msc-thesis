def remove_dirty_chars(s1, s2):
  return ''.join([c for c in s1 if c not in s2])  # or ''.join([c for c in s1 if s1.count(c) > s2.count(c)])