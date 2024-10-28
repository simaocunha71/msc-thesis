import re
def text_starta_endb(text: str) -> bool:
  pattern = re.compile(r'a.*b$')
  if pattern.match(text):
    return True
  return False

