
import re
def text_match_three(text):
  pattern = 'abbb'
  if re.search(pattern,  text):
    return True
  else:
    return False


