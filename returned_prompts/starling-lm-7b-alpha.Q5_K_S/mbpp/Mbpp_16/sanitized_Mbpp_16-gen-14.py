def text_lowercase_underscore(s):
  for c in s:
    if c.isupper() or c not in "_":
      return False
  return True