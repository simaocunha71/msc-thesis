def replace_spaces(s: str) -> str:
  new_s = ''
  for c in s:
    if c == ' ':
      new_s += '_'
    elif c == '_':
      new_s += ' '
    else:
      new_s += c
  return new_s