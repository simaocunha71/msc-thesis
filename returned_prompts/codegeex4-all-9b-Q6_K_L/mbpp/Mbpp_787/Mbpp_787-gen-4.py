import re
def text_match_three(text):
  pattern = re.compile(r'abbb')
  return bool(pattern.match(text))