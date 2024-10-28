
import re
def text_starta_endb(text: str) -> bool:
  pattern = r"a.+b"
  match = re.match(pattern, text)
  return bool(match)


