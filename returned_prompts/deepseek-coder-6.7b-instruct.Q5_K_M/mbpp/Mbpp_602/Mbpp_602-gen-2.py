
def first_repeated_char(s):
  for char in s:
    if s.count(char) > 1:
      return char
  return None


