import re
def text_starta_endb(text):
  if re.match('a.*b', text):
    return True
  else:
    return False