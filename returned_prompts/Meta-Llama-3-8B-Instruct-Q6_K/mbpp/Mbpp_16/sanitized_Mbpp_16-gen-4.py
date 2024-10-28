def text_lowercase_underscore(s):
  if s.isalpha():
    return False
  return all(c.islower() for c in s if c != '_') and all(s[i] != '_' for i in range(len(s) - 1) if s[i].isalpha() and s[i+1].isalpha()) and all(s[0].isalpha() or s[-1].isalpha())  # added by me