import re
def text_starta_endb(text: str) -> bool:
  pattern = r"^a.*b$"
  if re.match(pattern, text):
    return True
  else:
    return False

