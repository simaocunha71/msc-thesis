import re
def text_starta_endb(text: str) -> bool:
  pattern = r'a.*b$'
  if re.search(pattern, text):
    return True
  return False

