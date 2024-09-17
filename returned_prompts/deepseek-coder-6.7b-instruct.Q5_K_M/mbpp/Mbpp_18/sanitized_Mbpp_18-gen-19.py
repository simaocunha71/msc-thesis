def remove_dirty_chars(s1, s2):
  for c in s2:
    s1 = s1.replace(c, '')
  return s1