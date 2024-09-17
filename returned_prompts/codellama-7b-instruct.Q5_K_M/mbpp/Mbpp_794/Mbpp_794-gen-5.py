
import re
def text_starta_endb(text):
  return re.match(r"a.+b$", text)


