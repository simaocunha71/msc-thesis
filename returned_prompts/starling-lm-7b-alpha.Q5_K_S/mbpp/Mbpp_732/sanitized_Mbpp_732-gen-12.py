def replace_specialchar(s: str) -> str:
  s = s.replace(' ', ':')
  s = s.replace(',', ':')
  s = s.replace('.', ':')
  return s