
import re
def text_starta_endb(text: str) -> bool:
  if re.match("a.*b", text):
    return True
  return False


