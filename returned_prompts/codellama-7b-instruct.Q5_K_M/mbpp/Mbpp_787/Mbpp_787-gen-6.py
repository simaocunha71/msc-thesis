
import re
def text_match_three(text: str) -> bool:
  pattern = re.compile(r"a{3}b")
  if pattern.match(text):
    return True
  return False


