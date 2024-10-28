def text_match_three(s):
  if len(s) < 4:
    return False
  if s[0] != 'a' or s[1] != 'b' or s[2] != 'b' or s[3] != 'b':
    return False
  return True