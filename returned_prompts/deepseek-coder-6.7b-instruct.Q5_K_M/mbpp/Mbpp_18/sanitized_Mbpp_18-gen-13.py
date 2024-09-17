def remove_dirty_chars(s1, s2):
  return ''.join([char for char in s1 if char not in s2])