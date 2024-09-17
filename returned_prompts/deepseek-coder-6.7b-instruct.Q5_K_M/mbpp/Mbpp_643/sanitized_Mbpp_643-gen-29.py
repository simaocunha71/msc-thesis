import re
def text_match_wordz_middle(text):
  pattern = 'z'
  if re.search(pattern, text[1:-1]):
    return True
  else:
    return False