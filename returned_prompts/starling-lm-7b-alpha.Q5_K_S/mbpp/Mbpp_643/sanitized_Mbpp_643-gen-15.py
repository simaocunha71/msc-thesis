def text_match_wordz_middle(s: str):
  if s[0] == 'z' or s[-1] == 'z' or s.count('z') == 0:
    return False
  else:
    return True