def replace_specialchar(string: str) -> str:
  for ch in ['.', ',', ' ']:
    string = string.replace(ch, ':')
  return string