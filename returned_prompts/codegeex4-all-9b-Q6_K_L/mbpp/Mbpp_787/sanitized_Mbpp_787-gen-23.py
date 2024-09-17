import re
def text_match_three(text: str) -> bool:
  return bool(re.fullmatch(r"abbb", text))