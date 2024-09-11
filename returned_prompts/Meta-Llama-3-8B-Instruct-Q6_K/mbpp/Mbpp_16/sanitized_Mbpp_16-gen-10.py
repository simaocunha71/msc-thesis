def text_lowercase_underscore(s: str) -> bool:
  for i in range(len(s) - 1):
    if s[i].islower() and s[i+1] == '_':
      for j in range(i+2, len(s)):
        if not s[j].islower():
          return False
  return True