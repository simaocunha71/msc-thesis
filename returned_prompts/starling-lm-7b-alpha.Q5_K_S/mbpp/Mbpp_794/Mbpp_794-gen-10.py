
import re
def text_starta_endb(string:str) -> bool:
  if re.match("^a.*b$", string):
    return True
  else:
    return False


