def replace_specialchar(s):
  for c in ['.',',',' ']:
    if c in s:
      s = s.replace(c, ':')
  return s