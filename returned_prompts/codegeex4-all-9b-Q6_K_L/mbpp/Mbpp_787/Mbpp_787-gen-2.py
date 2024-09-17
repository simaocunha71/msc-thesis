import re
def text_match_three(text: str) -> bool:
  pattern = re.compile(r'abbb')
  match = pattern.fullmatch(text)
  if match:
    return True
  else:
    return False

