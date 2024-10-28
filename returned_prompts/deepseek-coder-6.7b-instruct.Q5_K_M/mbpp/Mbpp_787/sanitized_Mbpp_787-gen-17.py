import re
def text_match_three(text):
  pattern = 'ab{3}'
  if re.search(pattern,  text):
    return True
  else:
    return False