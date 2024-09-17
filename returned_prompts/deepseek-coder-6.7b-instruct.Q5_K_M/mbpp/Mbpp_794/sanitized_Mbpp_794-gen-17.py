import re
def text_starta_endb(text):
  return re.fullmatch('a.*b', text) is not None