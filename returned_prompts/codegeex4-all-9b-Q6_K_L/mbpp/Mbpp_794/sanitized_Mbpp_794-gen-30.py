import re
def text_starta_endb(s: str):
  if re.match(".*a.*b$", s):
    return True
  else:
    return False