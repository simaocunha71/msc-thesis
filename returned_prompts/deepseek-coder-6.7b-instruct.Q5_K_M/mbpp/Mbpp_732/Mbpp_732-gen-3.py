
def replace_specialchar(s):
  for char in s:
    if char in ' ,.':
      s = s.replace(char, ':')
  return s


