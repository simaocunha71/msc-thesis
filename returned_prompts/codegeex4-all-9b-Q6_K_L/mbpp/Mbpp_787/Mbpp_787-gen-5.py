import re
def text_match_three(s: str):
  pattern = r"abbb"
  if re.search(pattern, s):
    return True
  return False

