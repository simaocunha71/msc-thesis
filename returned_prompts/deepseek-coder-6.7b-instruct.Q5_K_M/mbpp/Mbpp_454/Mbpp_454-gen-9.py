
import re
def text_match_wordz(text):
  pattern = r'z'
  if re.search(pattern, text):
    return True
  else:
    return False


