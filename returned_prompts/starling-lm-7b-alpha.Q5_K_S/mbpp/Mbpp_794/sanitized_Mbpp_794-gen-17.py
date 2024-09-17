import re
def text_starta_endb(s:str) -> bool:
  if re.match(r'a.*b$', s) != None:
    return True
  else:
    return False