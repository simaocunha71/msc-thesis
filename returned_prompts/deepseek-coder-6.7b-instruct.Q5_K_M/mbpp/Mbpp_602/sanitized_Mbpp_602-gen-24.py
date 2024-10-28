def first_repeated_char(s):
  for ch in s:
    if s.count(ch) > 1:
      return ch
  return None