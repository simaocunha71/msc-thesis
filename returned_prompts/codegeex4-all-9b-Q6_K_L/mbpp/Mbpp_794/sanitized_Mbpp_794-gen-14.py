import re
def text_starta_endb(text):
  pattern = re.compile(r'a.*b$')
  return bool(pattern.match(text))