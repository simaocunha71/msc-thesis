import re
def text_match_three(text: str):
  pattern = re.compile(r"ab{3}")
  return bool(pattern.match(text))