
def replace_specialchar(s):
  for char in ['.',',',' ']:
    s = s.replace(char,':')
  return s


