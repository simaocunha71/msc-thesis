
import re
def text_match_three(text: str) -> bool:
  pattern = re.compile(r'a.{3}')
  return True if pattern.match(text) else False


