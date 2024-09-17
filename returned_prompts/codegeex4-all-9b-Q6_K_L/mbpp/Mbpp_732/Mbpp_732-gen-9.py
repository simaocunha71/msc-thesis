def replace_specialchar(s: str) -> str:
  special_chars = [' ', ',', '.']
  for char in special_chars:
    s = s.replace(char, ':')
  return s

