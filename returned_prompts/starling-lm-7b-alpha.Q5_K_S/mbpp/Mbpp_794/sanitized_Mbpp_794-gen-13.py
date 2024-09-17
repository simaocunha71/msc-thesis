import re
def text_starta_endb(s: str) -> bool:
  return re.match("^a.*b$", s) != None