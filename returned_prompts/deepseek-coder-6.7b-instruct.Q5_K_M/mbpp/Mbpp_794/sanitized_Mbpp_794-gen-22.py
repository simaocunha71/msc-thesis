import re
def text_starta_endb(text):
  return bool(re.fullmatch(r'a.*b$', text))